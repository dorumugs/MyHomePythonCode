from utils.log import logger
import pandas as pd
import numpy as np
from utils.database.elasticsearch_urils import QelasticSearch


class Export(object):
    def __init__(self, _logger):
        if _logger is None:
            self.logger = logger.setup("EXTRACT")
        else:
            self.logger = _logger
        self.qes = QelasticSearch(self.logger)

    def export_elasticsearch_func(self, index_nm, mapping, csv_file, target):
        self.qes.overwrite_index(index_nm, mapping)
        df = pd.read_csv(csv_file, sep='|', encoding='utf-8', low_memory=False)
        df = df.dropna()
        df = df.replace([np.inf, -np.inf], 0)
        self.logger.info(f"Import {target} Data")
        self.qes.parallel_bulk_insert(index_nm, self.qes.iter_source(target=target, index_nm=index_nm,
                                                                     dataframe=df))
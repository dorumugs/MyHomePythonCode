from utils.log import logger
from elasticsearch import Elasticsearch
import json
from datetime import date, timedelta
from elasticsearch import helpers
from config.elasticsearch.mappings_elasticsearch import *
from config.elasticsearch.fields_elasticsearch import *


class QelasticSearch(object):
    def __init__(self, _logger):
        if _logger is None:
            self.logger = logger.setup("EXPORT")
        else:
            self.logger = _logger

        with open('./config/elasticsearch/elastic_config', "r", encoding="UTF-8") as f:
            conf = json.loads(f.read())
        hosts = conf["hosts"]
        self.es = Elasticsearch(hosts=hosts)

    def get_info(self):
        return self.es.info(pretty=True)

    def show_index(self):
        return self.es.cat.indices(pretty=True)

    def create_index(self, index, mapping=None):
        if not self.es.indices.exists(index=index):
            if mapping is None:
                return self.es.indices.create(index=index, pretty=True)
            else:
                return self.es.indices.create(index=index, body=mapping, pretty=True)

    def overwrite_index(self, index, mapping=None):
        if self.es.indices.exists(index=index):
            self.delete_index(index=index)
        else:
            if mapping is None:
                return self.es.indices.create(index=index, pretty=True)
            else:
                return self.es.indices.create(index=index, body=mapping, pretty=True)

    def delete_index(self, index):
        if self.es.indices.exists(index=index):
            return self.es.indices.delete(index=index, pretty=True)

    def count_doc(self, index):
        return self.es.count(index=index, pretty=True)

    def show_schema(self, index):
        return self.es.indices.get_mapping(index=index, pretty=True)

    def doc_insert(self, index, body):
        return self.es.index(index=index, body=body, pretty=True)

    def parallel_bulk_insert(self, index, json_func):
        for success, info in helpers.parallel_bulk(self.es, json_func):
            if not success:
                print("Document failed : ", info)
        self.es.indices.refresh(index=index)

    def search_doc(self, index, batch_size=10000, data=None):
        if data is None:
            data = {"match_all": {}}
        else:
            data = {"match": data}
        body = {"size": batch_size,
                "query": data}
        return self.es.search(index=index, body=body)

    def field_date(self, target):
        today = date.today()
        date_str = today.strftime("%Y.%m.%d")
        index_nm, mapping = '', ''
        if target == 'ACTUAL':
            index_nm = REAL_ESTATE_MAPPING_AC['info']['index_nm']+'='+date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = REAL_ESTATE_MAPPING_AC['mapping']
        elif target == 'CHARTERED_RENT':
            index_nm = REAL_ESTATE_MAPPING_CH['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = REAL_ESTATE_MAPPING_CH['mapping']
        elif target == 'ACTUAL_PRE':
            index_nm = REAL_ESTATE_MAPPING_AC_PRE['info']['index_nm']+'='+date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = REAL_ESTATE_MAPPING_AC_PRE['mapping']
        elif target == 'CHARTERED_RENT_PRE':
            index_nm = REAL_ESTATE_MAPPING_CH_PRE['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = REAL_ESTATE_MAPPING_CH_PRE['mapping']
        elif target == 'AC_CH':
            index_nm = AC_CH_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = AC_CH_MAPPING['mapping']
        elif target == 'GDP':
            index_nm = GDP_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = GDP_MAPPING['mapping']
        elif target == 'POPULATION':
            index_nm = POPULATION_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = POPULATION_MAPPING['mapping']
        elif target == 'PRICE':
            index_nm = PRICE_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = PRICE_MAPPING['mapping']
        elif target == 'UNSOLD':
            index_nm = UNSOLD_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = UNSOLD_MAPPING['mapping']
        return index_nm, mapping

    def iter_source(self, target, index_nm, dataframe):
        self.logger.info(f"Target Name - {target}")
        if target == 'ACTUAL':
            for idx in dataframe.index:
                yield real_estate_ac_fields(index_nm, dataframe, idx)
        elif target == 'CHARTERED_RENT':
            for idx in dataframe.index:
                yield real_estate_ch_fields(index_nm, dataframe, idx)
        elif target == 'ACTUAL_PRE':
            for idx in dataframe.index:
                yield real_estate_ac_pre_fields(index_nm, dataframe, idx)
        elif target == 'CHARTERED_RENT_PRE':
            for idx in dataframe.index:
                yield real_estate_ch_pre_fields(index_nm, dataframe, idx)
        elif target == 'AC_CH':
            for idx in dataframe.index:
                yield ac_ch_fields(index_nm, dataframe, idx)
        elif target == 'GDP':
            for idx in dataframe.index:
                yield gdp_fields(index_nm, dataframe, idx)
        elif target == 'POPULATION':
            for idx in dataframe.index:
                yield population_fields(index_nm, dataframe, idx)
        elif target == 'PRICE':
            for idx in dataframe.index:
                yield price_fields(index_nm, dataframe, idx)
        elif target == 'UNSOLD':
            for idx in dataframe.index:
                yield unsold_fields(index_nm, dataframe, idx)

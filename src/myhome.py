from config.setting import *
from src.extract.et import Extract
from src.transform.ts import Transform
from src.export.ep import Export
from utils.database.elasticsearch_urils import QelasticSearch


class MyHome(object):
    def __init__(self, _logger):
        self.logger = _logger
        self.transform = Transform(self.logger)
        self.extract = Extract(self.logger)
        self.export = Export(self.logger)
        self.qes = QelasticSearch(self.logger)

    def real_estate(self):
        self.logger.info("code initializing")
        codes = self.extract.read_code_file(CODE_FILE_NAME)
        self.logger.info("code initialized : " + str(len(codes)))
        key = open('./config/tx/ServiceKey.txt')
        key = key.readlines()[0]
        selected_month = '2015-10'
        self.logger.info("data extract" + ' - ' + selected_month)
        self.extract.make_tx_df(ACTUAL_TX_URL, key, codes, selected_month, df_type="actual_tx")
        self.extract.make_tx_df(CHARTERED_RENT_URL, key, codes, selected_month, df_type="chartered_rent")

    def real_estate_pre(self):
        self.logger.info("gzip to csv")
        self.transform.gzip_to_csv()
        self.logger.info("TX preprocessing")
        self.transform.preprocessing(pre_type='TX')
        self.logger.info("TX End")
        self.logger.info("TX ALL preprocessing")
        self.transform.preprocessing(pre_type='TX_ALL_PRE')
        self.logger.info("TX ALL End")

    def get_curl_data(self):
        self.logger.info("REGION_CODE_FULL : Start")
        self.extract.get_data_by_curl(get_type='REGION_CODE_FULL')
        self.transform.preprocessing(pre_type='REGION_CODE_FULL')
        self.logger.info("POPULATION : Start")
        self.extract.get_data_by_curl(get_type='POPULATION')
        self.transform.preprocessing(pre_type='POPULATION')
        self.logger.info("REGION + POPULATION : Start")
        self.transform.preprocessing(pre_type='REGION_POP')
        self.logger.info("GDP : Start")
        self.extract.get_data_by_curl(get_type='GDP')
        self.transform.preprocessing(pre_type='GDP')
        self.logger.info("UNSOLD : Start")
        self.extract.get_data_by_curl(get_type='UNSOLD')
        self.transform.preprocessing(pre_type='UNSOLD')
        self.logger.info("PRICE : Start")
        self.extract.get_data_by_curl(get_type='PRICE')
        self.transform.preprocessing(pre_type='PRICE')

    def export_elasticsearch(self):
        target = 'AC_CH'
        index_nm, mapping = self.qes.field_date(target=target)
        csv = './data/csv/ac_ch.csv'
        self.export.export_elasticsearch_func(index_nm, mapping, csv, target)

        target = 'GDP'
        index_nm, mapping = self.qes.field_date(target=target)
        csv = './data/csv/GDP_pre.csv'
        self.export.export_elasticsearch_func(index_nm, mapping, csv, target)

        target = 'POPULATION'
        index_nm, mapping = self.qes.field_date(target=target)
        csv = './data/csv/population_pre.csv'
        self.export.export_elasticsearch_func(index_nm, mapping, csv, target)

        target = 'PRICE'
        index_nm, mapping = self.qes.field_date(target=target)
        csv = './data/csv/PRICE_pre.csv'
        self.export.export_elasticsearch_func(index_nm, mapping, csv, target)

        target = 'UNSOLD'
        index_nm, mapping = self.qes.field_date(target=target)
        csv = './data/csv/UNSOLD_pre.csv'
        self.export.export_elasticsearch_func(index_nm, mapping, csv, target)

        target = 'ACTUAL_PRE'
        index_nm, mapping = self.qes.field_date(target=target)
        csv = './data/output/final_files/pre_actual_tx_v1_pre.csv'
        self.export.export_elasticsearch_func(index_nm, mapping, csv, target)

        target = 'CHARTERED_RENT_PRE'
        index_nm, mapping = self.qes.field_date(target=target)
        csv = './data/output/final_files/pre_chartered_rent_v1_pre.csv'
        self.export.export_elasticsearch_func(index_nm, mapping, csv, target)

        # target = 'ACTUAL'
        # index_nm, mapping = self.qes.field_date(target=target)
        # csv = './data/output/final_files/pre_actual_tx_v1.csv'
        # self.export.export_elasticsearch_func(index_nm, mapping, csv, target)

        # target = 'CHARTERED_RENT'
        # index_nm, mapping = self.qes.field_date(target=target)
        # csv = './data/output/final_files/pre_chartered_rent_v1.csv'
        # self.export.export_elasticsearch_func(index_nm, mapping, csv, target)





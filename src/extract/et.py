from utils.log import logger
from config.setting import *
from config.population import *
from config.prices import *
from config.unsold import *
import pandas as pd
import requests
import bs4
import os
import json
import calendar


class Extract(object):

    def __init__(self, _logger):
        if _logger is None:
            self.logger = logger.setup("EXTRACT")
        else:
            self.logger = _logger

    @staticmethod
    def read_code_file(file_name):
        csv = pd.read_csv('./data/csv/code.csv', delimiter="\t")
        csv["code"] = csv.법정동코드.apply(lambda x: str(x)[0:5])
        codes = list(set(csv.code.to_list()))
        return codes

    @staticmethod
    def df_for_date(rows):
        row_list = []
        name_list = []
        column_list = []
        rows_len = len(rows)
        for i in range(0, rows_len):
            columns = rows[i].find_all()

            columns_len = len(columns)
            for j in range(0, columns_len):
                if i == 0:
                    name_list.append(columns[j].name)
                eachColumn = columns[j].text
                column_list.append(eachColumn)
            row_list.append(column_list)
            column_list = []

        df = pd.DataFrame(row_list, columns=name_list)
        return df

    def request_api(self, tx_columns, url, service_key, codes, date):
        df = pd.DataFrame(columns=tx_columns)
        for code in codes:
            payload = "serviceKey=" + service_key + "&" \
                      + "LAWD_CD=" + code + "&" \
                      + "DEAL_YMD=" + date
            res = requests.get(url + payload).text
            xmlobj = bs4.BeautifulSoup(res, 'lxml-xml')
            rows = xmlobj.findAll('item')
            each_df = self.df_for_date(rows)
            if each_df.shape[0] != 0:
                each_df = each_df[tx_columns]
                df = pd.concat([df, each_df], axis=0)
        return df

    @staticmethod
    def create_date_range(selected_month):
        year_sm = selected_month.split('-')[0]
        day_sm = selected_month.split('-')[1]
        day_end = calendar.monthrange(int(year_sm), int(day_sm))
        date_list = pd.date_range(start=f'{selected_month}-01', end=f'{selected_month}-{day_end[1]}')
        date_list = list(set(date_list.format(formatter=lambda x: x.strftime("%Y%m"))))
        return date_list

    def make_tx_df(self, url, service_key, codes, selected_month, df_type):
        date_list = self.create_date_range(selected_month)
        if df_type == "actual_tx":
            df = pd.DataFrame(columns=ACTUAL_TX_COLUMNS)
        elif df_type == "chartered_rent":
            df = pd.DataFrame(columns=CHARTERED_RENT_TX_COLUMNS)
        else:
            df = pd.DataFrame()

        for date in date_list:
            if df_type == "actual_tx":
                each_df = self.request_api(ACTUAL_TX_COLUMNS, url, service_key, codes, date)
                each_df = each_df[ACTUAL_TX_COLUMNS]
                df = pd.concat([df, each_df], axis=0)
                self.logger.info(f"{date} actual_tx")
                df.to_parquet("./data/output/actual_tx/"+"df_" + str(date) + ".gzip", compression="gzip")
            elif df_type == "chartered_rent":
                each_df = self.request_api(CHARTERED_RENT_TX_COLUMNS, url, service_key, codes, date)
                each_df = each_df[CHARTERED_RENT_TX_COLUMNS]
                df = pd.concat([df, each_df], axis=0)
                self.logger.info(f"{date} chartered_rent")
                df.to_parquet("./data/output/chartered_rent/" + "df_" + str(date) + ".gzip", compression="gzip")
        return df

    @staticmethod
    def get_kosis_data(get_type, csv, url, headers, cookies, data):
        response = requests.get(url, headers=headers, cookies=cookies, data=data)
        text = json.loads(response.text)
        res_file = text['file']
        if get_type == 'UNSOLD':
            UNSOLD_DOWN_URL = unsold_url(res_file)
            response = requests.get(UNSOLD_DOWN_URL, headers=UNSOLD_DOWN_HEADERS, cookies=UNSOLD_DOWN_COOKIES, data=UNSOLD_DOWN_DATA)
        elif get_type == 'PRICE':
            PRICES_DOWN_DATA=make_prices_down_data(res_file)
            response = requests.get(PRICE_DOWN_URL, headers=PRICES_HEADERS, cookies=PRICES_COOKIES, data=PRICES_DOWN_DATA)
        elif get_type == 'POPULATION':
            POPULATION_DOWN_DATA=make_population_down_data(res_file)
            response = requests.get(POPULATION_DOWN_URL, headers=POPULATION_DOWN_HEADER, cookies=POPULATION_DOWN_COOKIES, data=POPULATION_DOWN_DATA)

        with open(csv, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=1024):
                fd.write(chunk)
        # f = pd.read_csv("./data/csv/UNSOLD.csv", encoding='cp949')

    def get_data_by_curl(self, get_type):
        if get_type == 'GDP':
            response = requests.post(GDP_URL, headers=GDP_HEADERS, cookies=GDP_COOKIES, data=GDP_DATA)
            os.makedirs("./data/xls/", exist_ok=True)
            with open("./data/xls/GDP.xls", 'wb') as fd:
                for chunk in response.iter_content(chunk_size=1024):
                    fd.write(chunk)
            df = pd.read_excel("./data/xls/GDP.xls", index_col=0)
            df.T.to_csv("./data/csv/GDP.csv", sep='|', na_rep='NaN', index=False)
        elif get_type == 'REGION_CODE_FULL':
            response = requests.get(REGION_CODE_FULL_URL, headers=REGION_FULL_HEADERS, cookies=REGION_FULL_COOKIES)
            with open("./data/csv/REGION_CODE_FULL.zip", 'wb') as fd:
                for chunk in response.iter_content(chunk_size=1024):
                    fd.write(chunk)
        elif get_type == 'POPULATION':
            csv = "./data/csv/population.csv"
            self.get_kosis_data(get_type, csv, POPULATION_URL, POPULATION_HEADERS, POPULATION_COOKIES, POPULATION_DATA)
        elif get_type == 'UNSOLD':
            csv = "./data/csv/UNSOLD.csv"
            self.get_kosis_data(get_type, csv, UNSOLD_URL, UNSOLD_HEADERS, UNSOLD_COOKIES, UNSOLD_DATA)
        elif get_type == 'PRICE':
            csv = "./data/csv/PRICE.csv"
            self.get_kosis_data(get_type, csv, PRICES_URL, PRICES_HEADERS, PRICES_COOKIES, PRICES_DATA)



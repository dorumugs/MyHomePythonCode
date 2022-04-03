from utils.log import logger
from sys import version
from platform import platform
from src.myhome import MyHome


# Logging Set
logger = logger.setup_logger("[MyHome Python]")
logger.info("Python Version -- " + str(version).replace('\n', ' '))
logger.info("OS Version -- " + str(platform()))

if __name__ == "__main__":
    my_home = MyHome(logger)
    # my_home.get_curl_data() # 데이터 가져오기
    # my_home.real_estate() # 실거래, 전세가 가져오기
    # my_home.real_estate_pre() # 데이터 전처리 하기
    my_home.export_elasticsearch()

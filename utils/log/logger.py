import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name, log_level='INFO'):
    """
        로그를 남기기위한 로거
    :param name: (str) 로거의 이름
    :param log_level: (str) 로거 레벨
    :return: (logging) 로거
    """
    # logger config
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    # log format
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    # file config
    # file_max_bytes = 100 * 1024 *1024
    # file_handler = RotatingFileHandler(filename='./logs/run.log', maxBytes=file_max_bytes, backupCount=10)
    # file_handler.setFormatter(formatter)
    # base config
    base_handler = logging.StreamHandler()
    base_handler.setFormatter(formatter)
    # logger mapping
    logger.addHandler(base_handler)
    # logger.addHandler(file_handler)
    return logger

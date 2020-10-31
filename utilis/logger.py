import logging


class Log:
    @staticmethod
    def log_msg():
        logger = logging.getLogger('Testcases')
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        file = logging.FileHandler(r'C:\Users\arun\PycharmProjects\hybrid\logs\file.log')
        logger.addHandler(file)
        file.setFormatter(formatter)
        return logger


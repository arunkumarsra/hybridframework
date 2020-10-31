from pageobject.base import Login
from utilis.read_config import *
from utilis.logger import Log
from utilis.data_driven import DataDriven


class TestLogin:
    logger = Log.log_msg()

    def test_data_driven(self, method):
        self.driver = method
        self.b = Login(self.driver)
        self.b.url(get_values('data', 'base'))
        self.logger.info('*****Started the module for Tc_002*****')
        self.logger.info('started the data driven testing')
        self.status = []
        for x in range(2, DataDriven.get_rows()+1):
            self.username = DataDriven.get_value(rows=x, columns=1)
            self.password = DataDriven.get_value(rows=x, columns=2)
            self.condition = DataDriven.get_value(rows=x, columns=3)
            self.b.text_box(get_values('locators', 'log_username'), data=self.username)
            self.b.text_box(get_values('locators', 'log_password'), data=self.password)
            self.b.btn(get_values('locators', 'log_btn'))
            self.expected = 'Dashboard / nopCommerce administration'
            self.actual = self.driver.title
            if self.expected == self.actual:
                if self.condition == 'Pass':
                    self.logger.info('passed')
                    self.b.btn(get_values('locators', 'log_out'))
                    self.status.append('pass')
                elif self.condition == 'Fail':
                    self.logger.info('failed')
                    self.status.append('Fail')
            elif self.expected != self.actual:
                if self.condition == 'Fail':
                    self.logger.info('passed')
                    self.status.append('pass')
                elif self.condition == 'Pass':
                    self.logger.info('Failed')
                    self.status.append('Fail')
        if 'Fail' not in self.status:
            self.logger.info('completed the data driven testing')
            self.logger.info('***** Finsihed the module for Tc_002*****')
        else:
            self.logger.info('DDT is failed')
        self.b.exit()








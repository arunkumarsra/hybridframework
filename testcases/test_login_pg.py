import pytest

from pageobject.base import Login
from utilis.read_config import *
from utilis.logger import Log
import time


class TestLogin:
    logger = Log.log_msg()

    def test_m1(self, method):
        self.logger.info('*****Started the module for Tc_001*****')
        self.logger.info('Tsting thr login page')
        self.driver = method
        self.a = Login(self.driver)
        self.a.url(get_values('data', 'base'))
        if self.driver.title == 'Your store. Login':
            assert True
            self.a.exit()
        else:
            self.driver.get_screenshot_as_file('sample.png')
            self.a.exit()

    def test_m2(self, method):
        self.driver = method
        self.b = Login(self.driver)
        self.b.url(get_values('data', 'base'))
        self.b.text_box(get_values('locators', 'log_username'), get_values('data', 'username'))
        self.b.text_box(get_values('locators', 'log_password'), get_values('data', 'password'))
        self.b.btn(get_values('locators', 'log_btn'))
        time.sleep(7)
        if self.driver.title == 'Dashboard / nopCommerce administration':
            assert True
            self.b.exit()
        else:
            self.driver.get_screenshot_as_file('invalid.png')
            self.b.btn(get_values('locators', 'log_out'))
            self.b.exit()
        self.logger.info('Tested the Login Page')
        self.logger.info('*****Finished the module for Tc_001*****')

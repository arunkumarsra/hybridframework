import random
import string
import time
from pageobject.base import Login
from utilis.read_config import get_values
from utilis.logger import Log


class TestCustomer:

    logger = Log.log_msg()

    def test_customer(self, method):
        self.logger.info('*****Started the module for Tc_003*****')
        self.logger.info('Started testing adding new customer')
        self.a = Login(method)
        self.a.url(get_values('data', 'base'))
        self.a.text_box(get_values('locators', 'log_username'), get_values('data', 'username'))
        self.a.text_box(get_values('locators', 'log_password'), get_values('data', 'password'))
        self.a.btn(get_values('locators', 'log_btn'))
        self.a.btn(get_values('customers', 'M_customer'))
        self.a.btn(get_values('customers', 'D_customer'))
        self.a.btn(get_values('customers', 'add_customer'))
        self.a.text_box(get_values('customers', 'email_customer'),
                        data=random_name()+'@gmail.com')
        self.a.text_box(get_values('customers', 'pass_customer'), data='testingsample')
        self.a.text_box(get_values('customers', 'fname_customer'), data='samplingcycle')
        self.a.text_box(get_values('customers', 'lname_customer'), data='neededlasst')
        self.a.text_box(get_values('customers', 'dob_customer'), data='01/01/2020')
        self.a.btn(get_values('customers', 'gender_customer'))
        self.a.text_box(get_values('customers', 'comp_customer'), data='accenture')
        self.a.btn(get_values('customers', 'op_newsletter_customer'))
        self.a.btn(get_values('customers', 'test_customer'))
        try:
            self.a.btn(get_values('customers', 'role_customer'))
            self.a.btn(get_values('customers', 'reg_customer'))
            self.a.btn(get_values('customers', 'gue_customer'))
        except Exception:
            print('Element is not interactable')
        finally:
            self.a.drop_down(get_values('customers', 'mang_ven_customer'))
        time.sleep(3)
        self.a.btn(get_values('customers', 'save_customer'))
        time.sleep(7)
        self.logger.info('***** Finished the module for Tc_003 *****')
        self.logger.info('Completed the testing of adding new customer')
        self.msg = self.a.driver.find_element_by_tag_name('body').text
        if 'The new customer has been added successfully.' in self.msg:
            assert True
        self.a.exit()


def random_name(word=7, char=string.ascii_lowercase):
    return ''.join(random.choice(char) for x in range(word))

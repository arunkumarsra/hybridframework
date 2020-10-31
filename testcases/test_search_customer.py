from utilis.read_config import get_values
from pageobject.base import Login


class TestSearchCustomer:

    def test_customer_search(self, method):
        self.c = Login(method)
        self.c.url(get_values('data', 'base'))
        self.c.text_box(get_values('locators',
                                   'log_username'), data=get_values('data', 'username'))
        self.c.text_box(get_values('locators', 'log_password'), data=get_values('data', 'password'))
        self.c.btn(get_values('locators', 'log_btn'))
        self.c.btn(get_values('customers', 'M_customer'))
        self.c.btn(get_values('customers', 'D_customer'))
        self.c.text_box(get_values('search', 'l_name'), data='Gates')
        self.c.btn(get_values('search', 'search_customer'))
        self.table = self.c.get_element(get_values('search', 'table'))
        self.row = self.c.len_elements(get_values('search', 'rows'))
        self.column = self.c.len_elements(get_values('search', 'columns'))
        self.check = self.c.table(name='steve_gates@nopCommerce.com', rows=self.row)
        assert True == self.check
        self.c.exit()

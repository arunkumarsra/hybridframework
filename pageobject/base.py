from selenium.webdriver.support.select import Select


class Login:

    def __init__(self, driver):
        self.driver = driver

    def url(self, url):
        self.driver.get(url)

    def text_box(self, ele, data):
        self.driver.find_element_by_xpath(ele).clear()
        self.driver.find_element_by_xpath(ele).send_keys(data)

    def btn(self, ele):
        self.driver.find_element_by_xpath(ele).click()

    def exit(self):
        self.driver.quit()

    def drop_down(self, ele):
        x = self.driver.find_element_by_xpath(ele)
        a = Select(x)
        a.select_by_visible_text('Vendor 1')

    def get_element(self, ele):
        self.driver.find_element_by_xpath(ele)

    def len_elements(self, ele):
        return len(self.driver.find_elements_by_xpath(ele))

    def table(self, name, rows):
        value = False
        for x in range(1, rows+1):
            table = self.driver.find_element_by_xpath("//table[@id='customers-grid']")
            names = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(x)+"]/td[2]").text
            if name == names:
                value = True
                break
        return value

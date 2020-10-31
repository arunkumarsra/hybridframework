import pytest
from selenium import webdriver


@pytest.fixture
def method(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        return driver
    else:
        print('enter a valid browser')


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')

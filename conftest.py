import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        print(f"Browser {browser_name} still is not implemented")
    yield driver
    print("\nquit browser..")
    driver.quit()

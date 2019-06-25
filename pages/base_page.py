import logging


logging.basicConfig(level=logging.INFO)


class BasePage:

    def __init__(self, driver, url, timeout=20):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)
        self.driver.set_page_load_timeout(timeout)
        self.driver.set_script_timeout(timeout)

    def open(self):
        logging.info(f'Open the page{self.url}')
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        if len(self.driver.find_elements(how, what)) > 0 and self.driver.find_elements(how, what)[0].is_displayed():
            return True
        return False

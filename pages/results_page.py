from .base_page import BasePage
from .locators import ResultsPageLocators
import logging
logging.basicConfig(level=logging.INFO)


class ResultsPage(BasePage):

    def should_be_search_result(self):
        logging.info('Verifying the announcement of a list of search results')
        assert self.is_element_present(*ResultsPageLocators.RESULT_TABLE), 'No results table'

    def should_be_link_in_first_five_results(self, link):
        logging.info(f'Check for the presence of the {link} in the links of the first five search results')
        for i in range(1, 6):
            assert len(self.driver.find_elements_by_xpath(
                f'//li[@class="serp-item"][{i}]//a[contains(@href,"{link}")]')) > 0, \
                f'Link "tensor.ru" is missing in {i} search result'

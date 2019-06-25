from .base_page import BasePage
from .locators import ResultsPageLocators


class ResultsPage(BasePage):

    def should_be_search_result(self):
        assert self.is_element_present(*ResultsPageLocators.RESULT_TABLE), 'Result table does not show'

    def should_be_link_in_first_five_results(self):
        for i in range(1, 6):
            assert len(self.driver.find_elements_by_xpath(
                f'//li[@class="serp-item"][{i}]//a[contains(@href,"tensor.ru")]')) > 0, \
                f'link "tensor.ru" missing in {i} result'

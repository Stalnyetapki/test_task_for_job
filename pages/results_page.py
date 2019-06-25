from .base_page import BasePage
from .locators import ResultsPageLocators
import logging
logging.basicConfig(level=logging.INFO)


class ResultsPage(BasePage):

    def should_be_search_result(self):
        logging.info('Проверяем, что объявился список результатов поиска')
        assert self.is_element_present(*ResultsPageLocators.RESULT_TABLE), 'Таблица результатов отсутствует'

    def should_be_link_in_first_five_results(self):
        logging.info('Ищем вхождения "tensor.ru" в ссылках первых пяти результатов поиска')
        for i in range(1, 6):
            assert len(self.driver.find_elements_by_xpath(
                f'//li[@class="serp-item"][{i}]//a[contains(@href,"tensor.ru")]')) > 0, \
                f'Ссылка "tensor.ru" отсутствует в {i} результате поиска'

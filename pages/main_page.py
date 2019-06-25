from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
import logging


logging.basicConfig(level=logging.INFO)


class MainPage(BasePage):

    def go_to_images_page(self):
        logging.info('Кликаем по ссылке Яндекс Картинки')
        link = self.driver.find_element(*MainPageLocators.IMAGES_LINK)
        link.click()

    def should_be_images_link(self):
        logging.info('Проверяем, что ссылка на ЯндексКартинки присутствует на главной странице')
        assert self.is_element_present(*MainPageLocators.IMAGES_LINK), 'Ссылка на Яндекс Картинки отсутствует'

    def should_be_search_bar(self):
        logging.info('Проверяем, что строка поиска присутствует')
        assert self.is_element_present(*MainPageLocators.SEARCH_INPUT), 'Отсутствует строка поиска'

    def input_text_in_search_bar(self, text):
        logging.info(f'Вводим в строку поиска {text}')
        search_input = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(text)

    def should_be_table_with_tips(self):
        logging.info('Проверяем, что появился резудльтат запроса')
        assert self.is_element_present(*MainPageLocators.DIV_LIST), 'Отсутствует результаты запроса'

    def press_button_enter(self):
        logging.info('Нажимаем на кнопку Enter')
        search_input = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        search_input.send_keys(Keys.ENTER)

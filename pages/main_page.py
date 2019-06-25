from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
import logging


logging.basicConfig(level=logging.INFO)


class MainPage(BasePage):

    def go_to_pictures_page(self):
        logging.info('Click on the link Yandex Pictures')
        link = self.driver.find_element(*MainPageLocators.IMAGES_LINK)
        link.click()

    def should_be_link_to_pictures_page(self):
        logging.info('Check that the link to Yandex Pictures is on the main page.')
        assert self.is_element_present(*MainPageLocators.IMAGES_LINK), 'Link to Yandex Pictures is missing'

    def should_be_search_bar(self):
        logging.info('Check that the search string is present')
        assert self.is_element_present(*MainPageLocators.SEARCH_INPUT), 'Missing search bar'

    def input_text_in_search_bar(self, text):
        logging.info(f'Enter in the search bar {text}')
        search_input = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(text)

    def should_be_suggest_list(self):
        logging.info('Check the appearance of the query result')
        assert self.is_element_present(*MainPageLocators.SUGGEST_LIST), 'Missing query results'

    def press_button_enter(self):
        logging.info('Press the Enter button')
        search_input = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        search_input.send_keys(Keys.ENTER)

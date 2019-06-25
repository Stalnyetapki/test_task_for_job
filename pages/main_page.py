from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def go_to_images_page(self):
        link = self.driver.find_element(*MainPageLocators.IMAGES_LINK)
        link.click()

    def should_be_images_link(self):
        assert self.is_element_present(*MainPageLocators.IMAGES_LINK), 'Images link does not show'

    def should_be_search_bar(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_INPUT), 'No search bar'

    def input_text_in_search_bar(self, text):
        search_input = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(text)

    def should_be_table_with_tips(self):
        assert self.is_element_present(*MainPageLocators.DIV_LIST), 'Result List does not show'

    def press_button_enter(self):
        search_input = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        search_input.send_keys(Keys.ENTER)

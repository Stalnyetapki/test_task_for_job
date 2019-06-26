from .base_page import BasePage
from .locators import ImagesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


logging.basicConfig(level=logging.INFO)


class ImagesPage(BasePage):

    def should_be_picture_page_url(self):
        logging.info('Check for correct url address')
        assert 'https://yandex.ru/images/' == self.driver.current_url, \
            'Current address is not an address https://yandex.ru/images/'

    def open_first_picture(self):
        logging.info('Open the first picture')
        image = self.driver.find_element(*ImagesPageLocators.FIRST_PICTURE_IN_LIST)
        image.click()

    def should_be_open_image(self):
        logging.info('Check that the image is present and its size is greater than 0')
        self.wait_until_element_is_visible(10, ImagesPageLocators.PICTURE[0], ImagesPageLocators.PICTURE[1])
        assert self.is_element_present(*ImagesPageLocators.PICTURE), 'Image element does not show'

    def test_yandex_picture_slider(self):
        logging.info('Check the correct operation of the slider')

        # Запоминаем ссылку изображения
        first_img_link = self.driver.find_element(*ImagesPageLocators.PICTURE).get_attribute('src')

        logging.info('Производим поиск локатора правой стрелки слайдера и нажимаем на неe')
        # Производим поиск локатора правой стрелки слайдера и нажимаем на неe
        self.wait_until_element_is_visible(10, ImagesPageLocators.NAV_RIGHT[0], ImagesPageLocators.NAV_RIGHT[1])
        nav_right = self.driver.find_element(*ImagesPageLocators.NAV_RIGHT)
        nav_right.click()
        self.wait_until_element_is_visible(10, ImagesPageLocators.PICTURE[0], ImagesPageLocators.PICTURE[1])

        # Запоминаем ссылку изображения, на которую произошел переход
        second_img_link = self.driver.find_element(*ImagesPageLocators.PICTURE).get_attribute('src')

        # Выполняем проверку, что переход на следущую картинку произошел, сравнивая ссылки изображений
        assert first_img_link != second_img_link, 'The picture has not changed'

        logging.info('Производим поиск локатора левой стрелки слайдера и нажимаем на неe')
        # Производим поиск локатора левой стрелки слайдера и нажимаем на неe
        self.wait_until_element_is_visible(10, ImagesPageLocators.NAV_LEFT[0], ImagesPageLocators.NAV_LEFT[1])
        nav_left = self.driver.find_element(*ImagesPageLocators.NAV_LEFT)
        nav_left.click()
        self.wait_until_element_is_visible(10, ImagesPageLocators.PICTURE[0], ImagesPageLocators.PICTURE[1])

        # Запоминаем ссылку изображения, на которую произошел переход
        third_img_link = self.driver.find_element(*ImagesPageLocators.PICTURE).get_attribute('src')

        # Проверяем, что произошел переход на первое изоюражение
        assert first_img_link == third_img_link, 'The images on the first page and current page are different.'

    def wait_until_element_is_visible(self, timeout, search_by, locator):
        # Ожиданием, пока элемент появится в DOM и будет видимым (его размер будет больше 0)
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(
            (search_by, locator)))

from .base_page import BasePage
from .locators import ImagesPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImagesPage(BasePage):

    def should_be_images_page_url(self):
        # проверка на корректный url адрес
        assert 'https://yandex.ru/images/' == self.driver.current_url, 'current url is not a url of images page'

    def open_first_picture(self):
        # Открыть первую картинку
        image = self.driver.find_element(*ImagesPageLocators.FIRST_PICTURE_IN_LIST)
        image.click()

    def should_be_open_image(self):
        # проверка на то, что изображение присутствует и его размер больше 0
        image = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-il="image__wrap"]')))
        assert self.is_element_present(*ImagesPageLocators.PICTURE), 'Image element does not show'

    def test_navbar_yandex(self):
        # Запоминаем ссылку изображения
        first_img_link = self.driver.find_element(*ImagesPageLocators.PICTURE).get_attribute('src')
        # Производим поиск локатора правой стрелки слайдера и нажимаем на неe
        nav_right = self.driver.find_element(*ImagesPageLocators.NAV_RIGHT)
        nav_right.click()
        # Запоминаем ссылку изображения, на которую произошел переход
        second_img_link = self.driver.find_element(*ImagesPageLocators.PICTURE).get_attribute('src')
        # Выполняем проверку, что переход на следущую картинку произошел, сравнивая ссылки изображений
        assert first_img_link != second_img_link, 'Picture does not change'
        # Производим поиск локатора левой стрелки слайдера и нажимаем на неe
        nav_left = self.driver.find_element(*ImagesPageLocators.NAV_LEFT)
        nav_left.click()
        # Запоминаем ссылку изображения, на которую произошел переход
        third_img_link = self.driver.find_element(*ImagesPageLocators.PICTURE).get_attribute('src')
        # Проверяем, что произошел переход на первое изоюражение
        assert first_img_link == third_img_link, 'Links are not equal'

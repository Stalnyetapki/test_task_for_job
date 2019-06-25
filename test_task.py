from .pages.main_page import MainPage
from .pages.images_page import ImagesPage
from .pages.results_page import ResultsPage


homepage_url = 'https://yandex.ru/'


def test_yandex_search(driver):
    page = MainPage(driver, homepage_url)
    # Переходим на главную страницу яндекса
    page.open()
    # Проверка наличия инпута для поиска
    page.should_be_search_bar()
    # Вводим слово "Тензор" в поиск
    page.input_text_in_search_bar('Тензор')
    page.should_be_table_with_tips()
    page.press_button_enter()
    results_page = ResultsPage(driver, driver.current_url)
    results_page.should_be_search_result()
    results_page.should_be_link_in_first_five_results()


def test_section_yandex_pictures(driver):
    page = MainPage(driver, homepage_url)
    # Переходим на главную страницу яндекса
    page.open()
    # Проверяем присутствие ссылки "Картинки"
    page.should_be_images_link()
    # Переходим в раздел Картинки
    page.go_to_images_page()
    images_page = ImagesPage(driver, driver.current_url)
    # проверка что ссылка корректна
    images_page.should_be_images_page_url()
    # открываем первую картинку
    images_page.open_first_picture()
    # проверяем, что она открылась (что элемент присутствует на странице и его размер больше нуля)
    images_page.should_be_open_image()
    # Проверяем работу слайдера
    images_page.test_navbar_yandex()



























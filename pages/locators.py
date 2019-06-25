from selenium.webdriver.common.by import By


class MainPageLocators:
    IMAGES_LINK = (By.CSS_SELECTOR, '[data-id="images"]')
    SEARCH_INPUT = (By.ID, 'text')
    DIV_LIST = (By.CLASS_NAME, 'popup__content')


class ImagesPageLocators:
    FIRST_PICTURE_IN_LIST = (By.CSS_SELECTOR,
                             'div.cl-masonry__column:nth-child(1)>.cl-teaser:nth-child(1)>.cl-teaser__wrap>a')
    PICTURE = (By.CSS_SELECTOR, '[data-il="image__wrap"]')
    NAV_RIGHT = (By.CLASS_NAME, 'cl-layout__nav__right')
    NAV_LEFT = (By.CLASS_NAME, 'cl-layout__nav__left')


class ResultsPageLocators:
    RESULT_TABLE = (By.CSS_SELECTOR, '[aria-label="Результаты поиска"]')



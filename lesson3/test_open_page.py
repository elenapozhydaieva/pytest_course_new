from selenium.webdriver.common.by import By

MAIN_PAGE_URL = "https://victoretc.github.io/selenium_waits/"
TITLE = By.CSS_SELECTOR, "h1"


#  Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/
def test_open_page(driver):
    driver.get(MAIN_PAGE_URL)
    assert driver.current_url == "https://victoretc.github.io/selenium_waits/"


#   Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium".
def test_title(driver):
    driver.get(MAIN_PAGE_URL)
    title_element = driver.find_element(*TITLE)
    assert title_element.text == "Практика с ожиданиями в Selenium"



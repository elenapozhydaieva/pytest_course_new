from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

MAIN_PAGE_URL = "https://victoretc.github.io/selenium_waits/"
TITLE = By.CSS_SELECTOR, "h1"
START_TESTING_BUTTON = By.CSS_SELECTOR, "#startTest"
LOGIN_FIELD = By.CSS_SELECTOR, "#login"
PASSWORD_FIELD = By.CSS_SELECTOR, "#password"
CHECKBOX_AGREE = By.CSS_SELECTOR, "#agree"
REGISTRATION_BUTTON = By.CSS_SELECTOR, "#register"
SUCCESS_MESSAGE = By.CSS_SELECTOR, "#successMessage"


# Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/
def test_open_page(driver):
    driver.get(MAIN_PAGE_URL)
    assert driver.current_url == "https://victoretc.github.io/selenium_waits/"


# Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium".
def test_title(driver):
    driver.get(MAIN_PAGE_URL)
    title_element = driver.find_element(*TITLE)
    assert title_element.text == "Практика с ожиданиями в Selenium"


# Дождаться появления кнопки "Начать тестирование"
def test_button_start_testing(driver, wait):
    driver.get(MAIN_PAGE_URL)
    button_start_testing = wait.until(EC.visibility_of_element_located(START_TESTING_BUTTON))
    assert button_start_testing.is_displayed()


# Начать тестирование: Кликнуть по кнопке "Начать тестирование".
def test_click_button_start_testing(driver, wait):
    driver.get(MAIN_PAGE_URL)
    button_start_testing = wait.until(EC.element_to_be_clickable(START_TESTING_BUTTON))
    button_start_testing.click()


# Ввод логина: Ввести "login" в поле для логина.
# Ввод пароля: Ввести "password" в поле для пароля.
# Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
# Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
# Проверка загрузки: Удостовериться, что появился индикатор загрузки.
# Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
def test_registration(driver, wait):
    driver.get(MAIN_PAGE_URL)
    button_start_testing = wait.until(EC.element_to_be_clickable(START_TESTING_BUTTON))
    button_start_testing.click()
    login_field = wait.until(EC.element_to_be_clickable(LOGIN_FIELD))
    login_field.send_keys("login")
    password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD))
    password_field.send_keys("password")
    checkbox_agree = wait.until(EC.element_to_be_clickable(CHECKBOX_AGREE))
    checkbox_agree.click()
    registration_button = wait.until(EC.element_to_be_clickable(REGISTRATION_BUTTON))
    registration_button.click()
    success_message = wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
    assert success_message.is_displayed()



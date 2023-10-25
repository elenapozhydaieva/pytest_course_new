from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


def test_login_form_incorrect():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    search_message = WebDriverWait(driver, 3).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.error-message-container.error'),
        "Epic sadface: Username and password do not match any user in this service"))
    # time.sleep(5)
    assert search_message is True


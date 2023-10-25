import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def login(driver):
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


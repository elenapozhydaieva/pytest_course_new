from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

# Logout from the site
def test_logout():
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    menu_button = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    menu_button.click()
    time.sleep(2)

    logout_button = driver.find_element(By.XPATH, "//*[text()='Logout']")
    logout_button.click()
    time.sleep(2)
    assert driver.current_url == "https://www.saucedemo.com/"



# Checking the functionality of the "About" button in the menu
def test_about():
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    menu_button = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    menu_button.click()
    time.sleep(2)
    about_button = driver.find_element(By.XPATH, "//*[text()='About']")
    about_button.click()
    time.sleep(5)
    assert driver.current_url == "https://saucelabs.com/"



# Checking the functionality of the "Reset App State" button in the menu
def test_reset():
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    menu_button = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    menu_button.click()
    time.sleep(2)
    reset_button = driver.find_element(By.XPATH, "//*[text()='Reset App State']")
    reset_button.click()

    assert "shopping_cart_badge" not in driver.page_source


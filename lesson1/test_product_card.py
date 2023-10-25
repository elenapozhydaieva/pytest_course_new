import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


# Successful transition to the product card after clicking on the product image
def test_successful_transition_to_product_card_by_image():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    product_image = driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Backpack']")
    product_image.click()
    time.sleep(2)
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"



# Successful transition to the product card after clicking on the product name
def test_successful_transition_to_product_card_by_name():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    product_name = driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
    product_name.click()
    time.sleep(2)
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"



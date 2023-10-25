import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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


# Adding a product to the cart through the catalog
def test_add_to_cart_through_catalog(driver, login):
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)').click()
    count_cart_items = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge')
    assert count_cart_items.text == "6"



# Removing an item from your cart using the cart
def test_remove_from_cart(driver, login):
    driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)').click()
    cart_button = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge')
    cart_button.click()

    driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-bike-light').click()
    driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-fleece-jacket').click()
    driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '#remove-test\.allthethings\(\)-t-shirt-\(red\)').click()
    cart_items = driver.find_elements(By.XPATH, '//div[@class="cart_list"]/div[@class="cart_item"]')
    assert len(cart_items) == 0



# Adding a product to the cart from the product card
def test_add_to_cart_from_product_card(driver, login):
    driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']").click()
    add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    cart_button = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_button.click()
    cart_items = driver.find_elements(By.XPATH, '//div[@class="cart_list"]/div[@class="cart_item"]')
    assert len(cart_items) > 0


# Removing an item from the cart using the product card
def test_remove_from_cart_using_product_card(driver, login):
    driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']").click()
    time.sleep(2)
    add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-backpack').click()
    cart_button = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_button.click()
    cart_items = driver.find_elements(By.XPATH, '//div[@class="cart_list"]/div[@class="cart_item"]')
    assert len(cart_items) == 0

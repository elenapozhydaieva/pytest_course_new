import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


# Checking the filter functionality (A to Z)
def test_check_filter_A_to_Z():
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    inventory_list = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')
    # print(len(inventory_list))
    # print(inventory_list[0].text)
    assert "Sauce Labs Backpack" in inventory_list[0].text


# Checking the filter functionality (Z to A)
def test_check_filter_Z_to_A():
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    sort_container = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
    sort_container.click()
    sort_option = driver.find_element(By.XPATH, '//option[@value="za"]')
    sort_option.click()

    inventory_list = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')
    # print(len(inventory_list))
    # print(inventory_list[0].text)
    assert "Test.allTheThings() T-Shirt (Red)" in inventory_list[0].text


# Checking filter functionality (low to high)
def test_check_filter_low_to_high():
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    sort_container = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
    sort_container.click()
    sort_option = driver.find_element(By.XPATH, '//option[@value="lohi"]')
    sort_option.click()

    inventory_list = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')
    # print(len(inventory_list))
    # print(inventory_list[0].text)
    assert "Sauce Labs Onesie" in inventory_list[0].text


# Checking filter functionality (high to low)
def test_check_filter_high_to_low():
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    sort_container = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
    sort_container.click()
    sort_option = driver.find_element(By.XPATH, '//option[@value="hilo"]')
    sort_option.click()

    inventory_list = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')
    # print(len(inventory_list))
    # print(inventory_list[0].text)
    assert "Sauce Labs Fleece Jacket" in inventory_list[0].text


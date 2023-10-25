from selenium.webdriver.common.by import By


# Checking the filter functionality (A to Z)
def test_check_filter_A_to_Z(driver, login):
    inventory_list = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')
    assert "Sauce Labs Backpack" in inventory_list[0].text


# Checking the filter functionality (Z to A)
def test_check_filter_Z_to_A(driver, login):
    sort_container = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
    sort_container.click()
    sort_option = driver.find_element(By.XPATH, '//option[@value="za"]')
    sort_option.click()
    inventory_list = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')
    assert "Test.allTheThings() T-Shirt (Red)" in inventory_list[0].text


# Checking filter functionality (low to high)
def test_check_filter_low_to_high(driver, login):
    sort_container = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
    sort_container.click()
    sort_option = driver.find_element(By.XPATH, '//option[@value="lohi"]')
    sort_option.click()
    inventory_list = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')
    assert "Sauce Labs Onesie" in inventory_list[0].text


# Checking filter functionality (high to low)
def test_check_filter_high_to_low(driver, login):
    sort_container = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
    sort_container.click()
    sort_option = driver.find_element(By.XPATH, '//option[@value="hilo"]')
    sort_option.click()
    inventory_list = driver.find_elements(By.XPATH, '//div[@class="inventory_list"]/div[@class="inventory_item"]')
    assert "Sauce Labs Fleece Jacket" in inventory_list[0].text


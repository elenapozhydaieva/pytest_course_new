from selenium.webdriver.common.by import By


# Successful transition to the product card after clicking on the product image
def test_successful_transition_to_product_card_by_image(driver, login):
    product_image = driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Backpack']")
    product_image.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"


# Successful transition to the product card after clicking on the product name
def test_successful_transition_to_product_card_by_name(driver, login):
    product_name = driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
    product_name.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"



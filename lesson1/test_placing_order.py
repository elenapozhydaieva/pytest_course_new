from selenium.webdriver.common.by import By


# Placing an order using correct data
def test_place_order_correct_data(driver, login):
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    cart_button = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_button.click()
    checkout_button = driver.find_element(By.CSS_SELECTOR, '#checkout')
    checkout_button.click()

    first_name_field = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name_field.send_keys("Kate")
    last_name_field = driver.find_element(By.CSS_SELECTOR, '#last-name')
    last_name_field.send_keys("Kitty")
    postal_code_field = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    postal_code_field.send_keys("12345")
    continue_button = driver.find_element(By.CSS_SELECTOR, '#continue')
    continue_button.click()
    finish_button = driver.find_element(By.CSS_SELECTOR, '#finish')
    finish_button.click()
    order_is_finished = driver.find_element(By.CSS_SELECTOR, '.complete-header')
    assert order_is_finished.text == "Thank you for your order!"




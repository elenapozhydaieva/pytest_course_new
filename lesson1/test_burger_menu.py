from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Logout from the site
def test_logout(driver, login, wait):
    menu_button = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    menu_button.click()
    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Logout']")))
    logout_button.click()
    assert driver.current_url == "https://www.saucedemo.com/"


# Checking the functionality of the "About" button in the menu
def test_about(driver, login, wait):
    menu_button = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    menu_button.click()
    about_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='About']")))
    about_button.click()
    assert driver.current_url == "https://saucelabs.com/"


# Checking the functionality of the "Reset App State" button in the menu
def test_reset(driver, login, wait):
    menu_button = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    menu_button.click()
    reset_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Reset App State']")))
    reset_button.click()
    assert "shopping_cart_badge" not in driver.page_source


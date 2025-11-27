
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def add_product():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.amazon.in/")
    time.sleep(2)

    searchbox = driver.find_element(By.ID, "twotabsearchtextbox")
    searchbox.send_keys("iphone 16")
    time.sleep(2)

    search_btn = driver.find_element(By.ID, "nav-search-submit-button")
    search_btn.click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(2)

    add_to_cart_btn = driver.find_element(By.ID, "a-autoid-1-announce")
    time.sleep(2)
    add_to_cart_btn.click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, -300);")
    time.sleep(2)

    cart = driver.find_element(By.ID, "nav-cart")
    cart.click()
    time.sleep(2)

    driver.quit()

add_product()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from xPathLocator import *
asset = manage_assets()

# =================== Add Find ==============================
def add_Assets(driver):
    driver.find_element(By.XPATH,asset.add_find_btn).click()
    time.sleep(2)
    for i in range(9,11):
        driver.find_element(By.XPATH,asset.add_find).send_keys(i)
        time.sleep(4)
        driver.find_element(By.XPATH,asset.add_find_submit).click()
        time.sleep(6)
        
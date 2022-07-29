import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from xPathLocator import *
asset = manage_assets()
alert1 = alerts()

# =================== Add Find ==============================
def add_Assets(driver):
    driver.find_element(By.XPATH,asset.add_find_btn).click()
    time.sleep(2)
    for i in range(9,11):
        driver.find_element(By.XPATH,asset.add_find).send_keys(i)
        time.sleep(4)
        driver.find_element(By.XPATH,asset.add_find_submit).click()
        pass1 = driver.find_element(By.XPATH,alert1.add_find_alert).text
        print("======================================================",pass1)
        if pass1 == 'Asset registered successfully':
            return i
        else:
            driver.find_element(By.XPATH,asset.add_find).clear()
            driver.find_element(By.XPATH,asset.add_find_close).click()

        time.sleep(6)
        
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from xPathLocator import *
asset = manage_assets()

# driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
def add_Assets(driver):
    for i in range(1,10):
        driver.find_element(By.XPATH,asset.add_find_btn).click()
        time.sleep(2)
        driver.find_element(By.XPATH,asset.add_find).send_keys(i)
        time.sleep(4)
        driver.find_element(By.XPATH,asset.add_find_submit).click()
        time.sleep(4)
    return
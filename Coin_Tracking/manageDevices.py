import time
from selenium.webdriver.common.by import By
from xPathLocator import *
asset = manage_assets()
# driver = web_driver

class manage_Find():
    def add_Assets(self):
        x=10
        for i in range(x):
            web_driver.x(By.XPATH,asset.add_find_btn).click()
            time.sleep(4)
            web_driver(By.type,asset.add_find).send_keys(x)
            time.sleep(4)
            web_driver(By.XPATH,asset.add_find_submit).click()
            time.sleep(4)
            return
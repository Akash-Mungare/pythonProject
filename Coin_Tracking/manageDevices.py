import time
from selenium.webdriver.common.by import By
from xPathLocator import *
asset = manage_assets()
driver = web_driver

class manage_Find():
    def add_Assets(self):
        x=10
        for i in range(x):
            driver().x(By.XPATH,asset.add_find_btn).click()
            time.sleep(4)
            END_ELEMENT(By.type,asset.add_find).send_keys(x)
            time.sleep(4)
            END_ELEMENT(By.XPATH,asset.add_find_submit).click()
            time.sleep(4)
            return
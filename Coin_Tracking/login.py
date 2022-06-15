import time
from selenium import webdriver


class webelement():
    def xpathLocator(self):
        driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
        driver.get("https://ct.sensegiz.com/login")
        driver.maximize_window()
        driver.find_element_by_id("mat-input-0").send_keys('akash@gmail.com')
        time.sleep(4)
        driver.find_element_by_id("mat-input-1").send_keys('123')
        time.sleep(4)
        driver.find_element_by_class_name("mat-button-wrapper").click()
        time.sleep(4)
        driver.close()

findbyid = webelement()
findbyid.xpathLocator()
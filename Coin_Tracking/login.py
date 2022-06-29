import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from xPathLocator import *
# from index import selectorNum
xpath_L = login_all()
cred = credentials()
asset = manage_devices()
# num= selectorNum


class webelement():
    def login(self):
        list = ["1. MSIL Testing", "2.NewAT Testing", "3.CT Server"]
        print("List of server : ", list, "\n")

        print("Enter the value to select server:")
        x = int(input())
        # print("X : ",x)
        driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
        driver.maximize_window()
        if x == 1:
            driver.get(xpath_L.mst_baseUrl)
            time.sleep(2)
            driver.find_element(By.ID,xpath_L.user).send_keys(cred.mst_username)
            time.sleep(2)
            driver.find_element(By.ID,xpath_L.pwd).send_keys(cred.mst_password)
            time.sleep(2)
            driver.find_element(By.CLASS_NAME,xpath_L.lSubmit).click()
            time.sleep(2)

        elif x == 2:
            # driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
            # driver.maximize_window()
            driver.get(xpath_L.nat_baseUrl)
            time.sleep(2)
            driver.find_element(By.ID,xpath_L.user).send_keys(cred.nat_username)
            time.sleep(2)
            driver.find_element(By.ID,xpath_L.pwd).send_keys(cred.nat_password)
            time.sleep(2)
            driver.find_element(By.CLASS_NAME,xpath_L.lSubmit).click()
            time.sleep(8)
            driver.find_element(By.CLASS_NAME,asset.add_find).click()
            time.sleep(2)
        elif x == 3:
            # driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
            # driver.maximize_window()
            driver.get(xpath_L.ct_baseUrl)
            time.sleep(2)
            driver.find_element(By.ID,xpath_L.user).send_keys(cred.ct_userName)
            time.sleep(2)
            driver.find_element(By.ID,xpath_L.pwd).send_keys(cred.ct_password)
            time.sleep(2)
            driver.find_element(By.CLASS_NAME,xpath_L.lSubmit).click()
            time.sleep(6)
            driver.find_element(By.XPATH,asset.add_find).click()
            time.sleep(6)
        else:
            print("Wrong Input value!!! Please select correct input")
            return self.login()
        driver.close()

# findbyid = webelement()
# findbyid.xpathLocator()
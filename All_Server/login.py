import time
from pytest import param
from selenium import webdriver
from selenium.webdriver.common.by import By
from xPathLocator import *
from manageDevices import add_Assets
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from index import selectorNum
xpath_L = login_all()
cred = credentials()
# num= selectorNum

# @param.mark.functional
class webelement():
    # driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
    def web_login(self):
        list = ["1. NPT Testing", "2.NewAT Testing", "3.CT Testing"]
        print("List of server : ", list, "\n")

        print("Enter the value to select server:")
        x = int(input())
        # print("X : ",x)
        driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        # wait = WebDriverWait(driver, 10)
        if x == 1:
            driver.get(xpath_L.npt_baseUrl)
            # time.sleep(2)
            driver.find_element(By.ID,xpath_L.user).send_keys(cred.npt_username)
            # time.sleep(2)
            driver.find_element(By.ID,xpath_L.pwd).send_keys(cred.npt_password)
            # time.sleep(2)
            driver.find_element(By.CLASS_NAME,xpath_L.lSubmit).click()
            # time.sleep(2)
            add_Assets(driver)
            # time.sleep(2)

        elif x == 2:
            # driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
            # driver.maximize_window()
            driver.get(xpath_L.nat_baseUrl)
            # time.sleep(2)
            driver.find_element(By.ID,xpath_L.user).send_keys(cred.nat_username)
            # time.sleep(2)
            driver.find_element(By.ID,xpath_L.pwd).send_keys(cred.nat_password)
            # time.sleep(2)
            driver.find_element(By.CLASS_NAME,xpath_L.lSubmit).click()
            # time.sleep(8)
            add_Assets(driver)
            # time.sleep(2)
        elif x == 3:
            # driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
            # driver.maximize_window()
            driver.get(xpath_L.ct_baseUrl)
            # time.sleep(2)
            driver.find_element(By.ID,xpath_L.user).send_keys(cred.ct_userName)
            # time.sleep(2)
            driver.find_element(By.ID,xpath_L.pwd).send_keys(cred.ct_password)
            # time.sleep(2)
            driver.find_element(By.CLASS_NAME,xpath_L.lSubmit).click()
            # time.sleep(6)
            # EC.pre
            #     add_Assets(driver)
        else:
            print("Wrong Input value!!! Please select correct input")
            return self.login()
        driver.close()

# findbyid = webelement()
# findbyid.xpathLocator()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from xPathLocator import *
from manageDevices import add_Assets
# from index import selectorNum
xpath_L = login_all()
cred = credentials()
# num= selectorNum

class webelement():
    # driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
    def web_login(self):
        list = ["1. NPT Testing", "2.NewAT Testing", "3.CT Testing"]
        print("List of server : ", list, "\n")

        print("Enter the value to select server:")
        x = int(input())
        # print("X : ",x)
        driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe")
        driver.maximize_window()
        if x == 1:
            driver.get(xpath_L.npt_baseUrl)
            time.sleep(2)
            driver.find_element(By.ID,xpath_L.user).send_keys(cred.npt_username)
            time.sleep(2)
            driver.find_element(By.ID,xpath_L.pwd).send_keys(cred.npt_password)
            time.sleep(2)
            driver.find_element(By.CLASS_NAME,xpath_L.lSubmit).click()
            time.sleep(2)
            manage_device = add_Assets(driver)
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
            manage_device = add_Assets(driver)
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
            manage_device = add_Assets(driver)
        else:
            print("Wrong Input value!!! Please select correct input")
            return self.login()
        driver.close()

# findbyid = webelement()
# findbyid.xpathLocator()
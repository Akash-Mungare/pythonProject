# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


class login_all():
    ct_baseUrl = "https://ct.sensegiz.com/login"
    nat_baseUrl = "https://nat-test.sensegiz.com/login"
    mst_baseUrl = "https://mst.sensegiz.com/login"
    user = "mat-input-0"
    pwd = "mat-input-1"
    lSubmit = "mat-button-wrapper"
    # add_Find = "mat-focus-indicator mat-raised-button mat-button-base"

class credentials():
    ct_userName = "akash@gmail.com"
    ct_password = "123"
    nat_username = "akashmungare112@gmail.com"
    nat_password = "Akash@123"
    mst_username = "akashmungare5@gmail.com"
    mst_password = "Akash@123"

class manage_assets():
    add_find_btn = '//button[@class="mat-focus-indicator mat-raised-button mat-button-base"]' 
    add_find = "number"
    add_find_submit = '//button[@class="mat-focus-indicator mat-raised-button mat-button-base mat-primary"]'
    dasd
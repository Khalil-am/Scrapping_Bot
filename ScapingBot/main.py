import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_object = Service("/Users/khalil-am/Downloads/chromedriver")
driver = webdriver.Chrome(service=serv_object)  # driver.get("https://www.freecodecamp.org")
driver.get("https://opensource-demo.orangehrmlive.com/")
my_element = driver.find_element(By.ID, "txtUsername").send_keys("Admin")
my_element = driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
my_element = driver.find_element(By.NAME, "Submit").click()
act_title = driver.title
exp_title = "OrangeHRM"
if (act_title == exp_title):
    print("login test passed")
else:
    print("failed")

driver.close()

import time
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import Locators as locators

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://test.beeznests.com/")


def Login():
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()
    driver.find_element(By.ID, "email").send_keys("rashed.mahazi@gmail.com")
    sleep(2)
    driver.find_element(By.ID, "password").send_keys("123456789")
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()
    sleep(2)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("you have been successfully log in to Beeznests")
    else:
        print("Login failed")


def inactivity():
    inactivity_timeout = 60 * 5  # 5 minute
    time.sleep(inactivity_timeout)
    driver.refresh()
    assert driver.find_element(By.XPATH, "(//a[normalize-space()='REGISTER'])[1]").is_displayed()


Login()
inactivity()


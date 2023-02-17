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


def registration():
    driver.find_element(By.XPATH, locators.Register_Tab).click()
    sleep(2)
    driver.find_element(By.ID, locators.Email_Address).send_keys("rashed.mahazi@gmail.com")
    sleep(2)
    driver.find_element(By.ID, locators.Password).send_keys("123456789")
    driver.find_element(By.ID, locators.Confirm_Password).send_keys("123456789")
    sleep(2)
    # driver.find_element(By.XPATH, locators.Checkbox).click()
    sleep(2)
    driver.find_element(By.XPATH, locators.Register).click()
    Message = driver.find_element(By.XPATH, "//div[@class='tw-text-red-500 tw-pt-2 tw-text-sm']")
    assert Message.is_displayed()
    print(Message.text)


registration()
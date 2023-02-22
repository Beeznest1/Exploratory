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


def Logout_project():
    driver.find_element(By.XPATH, locators.PROJECTS).click()
    driver.find_element(By.XPATH, "//img[@alt='Ahmad Rashed Mahazi']").click()  # Dropdown menu
    sleep(2)
    driver.find_element(By.XPATH, locators.Logout_button).click()  # Logout button
    sleep(2)
    print("you are logout of Beeznests")


def Logout_Network():
    driver.find_element(By.XPATH, "//span[normalize-space()='NETWORK']").click()  # network page
    driver.find_element(By.XPATH, "//img[@alt='Ahmad Rashed Mahazi']").click()  # Dropdown menu
    sleep(2)
    driver.find_element(By.XPATH, locators.Logout_button).click()  # Logout button
    sleep(2)
    print("you are logout of Beeznests")


def Logout_bell():
    driver.find_element(By.XPATH, "//i[@class='fa fa-bell']").click()  # notification page
    driver.find_element(By.XPATH, "//img[@alt='Ahmad Rashed Mahazi']").click()  # Dropdown menu
    sleep(2)
    driver.find_element(By.XPATH, locators.Logout_button2).click()  # Logout button
    sleep(2)
    print("you are logout of Beeznests")


Login()
Logout_Network()
Login()
Logout_project()
Login()
Logout_bell()

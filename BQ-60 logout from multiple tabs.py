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


def another_tab():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://test.beeznests.com/")


def Logout():
    driver.find_element(By.XPATH, locators.DropDown_Menu).click()  # Dropdown menu
    sleep(2)
    driver.find_element(By.XPATH, locators.Logout_button).click()  # Logout button
    sleep(2)
    print("you are logout of Beeznests")


def first_tab():
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)
    driver.refresh()
    sleep(2)
    assert driver.find_element(By.XPATH, "(//a[normalize-space()='REGISTER'])[1]").is_displayed()
    print("you are successfully log out from both pages")


Login()
another_tab()
Logout()
first_tab()

driver.quit()

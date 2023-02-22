from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

import Locators as locators
from time import sleep


s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://test.beeznests.com/")


def Login():
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()
    sleep(1)
    driver.find_element(By.ID, "email").send_keys("rashed.mahazi@gmail.com")
    sleep(1)
    driver.find_element(By.ID, "password").send_keys("123456789")
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()
    sleep(3)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("you have been successfully log in to Beeznests")
    else:
        print("Login failed")


def PostProject():
    driver.find_element(By.XPATH, locators.PROJECTS).click()  # Project tab
    driver.find_element(By.XPATH, locators.Post_A_New_Project).click()
    driver.find_element(By.XPATH, locators.position).send_keys("Software Developer")  # Position Type
    sleep(2)
    driver.find_element(By.XPATH, locators.ProjectName).send_keys("Enjoy Dude")  # Project/Company Name
    driver.find_element(By.XPATH, locators.category).click()  # Category
    driver.find_element(By.XPATH, locators.Cloud_Computing_Engineers).click()
    sleep(3)


def Logout():
    driver.find_element(By.XPATH, "//img[@alt='Ahmad Rashed Mahazi']").click()  # Dropdown menu
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/header/div[1]/div/nav[2]/div/div/div/span").click()  # Logout button
    sleep(2)
    wait = WebDriverWait(driver, 10)
    popup = wait.until(driver.find_element(By.CSS_SELECTOR, ".popup-class").is_displayed())
    expected_text = "Do you want to save the changes"
    assert expected_text in popup.text


Login()
PostProject()
Logout()



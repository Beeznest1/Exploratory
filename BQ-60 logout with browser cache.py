from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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


def clear_browser_cache():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("chrome://settings/clearBrowserData")
    sleep(3)
    ActionChains(driver).send_keys(Keys.TAB * 1 + Keys.ENTER).perform()
    sleep(20)
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)
    driver.refresh()
    sleep(3)
    assert driver.find_element(By.XPATH, "(//a[normalize-space()='REGISTER'])[1]").is_displayed()
    print("you are successfully log out from both pages")


Login()
clear_browser_cache()

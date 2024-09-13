from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#could not run test due to robot test page
#driver.get('https://www.amazon.com/')

#check locator with $x("")
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "continue")
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.ID, "ap-other-signin-issues-link")
driver.find_element(By.ID, "createAccountSubmit")


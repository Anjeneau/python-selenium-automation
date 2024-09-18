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

driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR,"input#ap_customer_name")
driver.find_element(By.CSS_SELECTOR,"#ap_email")
driver.find_element(By.CSS_SELECTOR,"#ap_password")
driver.find_element(By.CSS_SELECTOR, "#auth-password-invalid-password-alert .a-alert-content")
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
driver.find_element(By.CSS_SELECTOR,"#continue")
driver.find_element(By.CSS_SELECTOR,"[href*='ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR,"[href*='ap_register_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR,"a.a-link-emphasis")

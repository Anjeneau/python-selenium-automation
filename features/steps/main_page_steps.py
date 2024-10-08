from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open Target page')
def open_target(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@when('Click Sign In Button')
def click_sign_in_button(context):
    context.app.header.click_sign_in()
    #context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()


@when('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.app.header.side_menu_signin()
    #context.driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()


@when('Find Benefits')
def find_benefits(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']").is_displayed()


@then('Verify Benefits')
def verify_benefits(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
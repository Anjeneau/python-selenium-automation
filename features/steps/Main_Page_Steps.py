from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@when('Click Sign In Button')
def click_sign_in_button(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(2)


@when('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()
    sleep(2)


@when('Find Benefits')
def find_benefits(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']").is_displayed()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    assert context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")


@then('Verify Benefits')
def verify_benefits(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
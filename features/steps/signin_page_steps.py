from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open sign in page')
def open_signin(context):
    context.driver.get('https://www.target.com/account')


@when('Click on Target terms and conditions link')
def click_ttc_link(context):
    context.app.signin_page.click_ttc_link()


@given('Store signin window')
def store_window(context):
    context.signin_window = context.app.signin_page.get_current_window()
    print('Original window: ', context.signin_window)


@when('Switch to the newly opened window')
def switch_to_window(context):
    context.app.signin_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_ttc_opened(context):
    context.app.signin_page.verify_ttc_opened()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.signin_page.verify_signin_form()
    #assert context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

@then('User can close new window and switch back to original')
def verify_user_close_new_window(context):
    context.app.signin_page.close()
    context.app.signin_page.switch_to_window_by_id(context.signin_window)

# @then('Close signin page')
# def close_page(context):
#     context.app.signin_page.close()
#
#
# @then('Return to original window')
# def switch_to_original(context):
#     context.app.signin_page.switch_to_window_by_id(context.signin_window)
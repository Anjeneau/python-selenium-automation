from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(2)


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='CartIcon']").click()
    sleep(2)

@when('Click Sign In Button')
def click_sign_in_button(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(2)

@when('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()
    sleep(2)

@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'

@then('Verify “Your cart is empty” message is shown')
def verify_empty_cart_message(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").is_displayed()

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    assert context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
from behave.runner import Context
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@when('Click on Cart icon')
def cart_click(context):
    context.app.header.click_cart()
   # context.driver.find_element(By.CSS_SELECTOR, "[data-test*='CartIcon']").click()


@when('Click Add to Cart button')
def click_cart_button(context):
    context.app.cart_page.add_to_cart()
    #context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    sleep(7)
# my computer can runs test extremely slow with explicit wait


@when('Confirm Add to cart')
def confirm_cart(context):
    context.app.cart_page.confirm_add_to_cart()
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']").click()


@when('View Cart')
def view_cart(context):
    context.app.cart_page.view_cart_checkout()
    #context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    sleep(4)


@then('Verify “Your cart is empty” message is shown')
def verify_empty_cart_message(context):
    context.app.cart_page.verify_cart_empty()
    #assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").is_displayed()


@then('Verify cart has {amount} item')
def verify_cart_has_item(context, amount):
    context.app.cart_page.verify_cart_item_amount(amount)
    #cart_sum = context.driver.find_element(By.CSS_SELECTOR, "[class='sc-93ec7147-3 fUVkzh']").text
    #assert f'{amount} item' in cart_sum


@then('Verify cart has correct product')
def verify_cart_has_correct_product(context):
    context.app.cart_page.verify_correct_product()
    #actual_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='cartItem']").text
    #print(f'Actual product in cart name: {actual_name}')
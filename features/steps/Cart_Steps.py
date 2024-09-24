from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Cart icon')
def cart_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='CartIcon']").click()
    sleep(4)


@when('Click Add to Cart button')
def click_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    sleep(6)


@when('Confirm Add to cart')
def confirm_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']").click()
    sleep(6)

@when('View Cart')
def view_cart(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    sleep(4)

@then('Verify “Your cart is empty” message is shown')
def verify_empty_cart_message(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").is_displayed()


@then('Verify cart has {amount} item')
def verify_cart_has_item(context, amount):
    cart_sum = context.driver.find_element(By.CSS_SELECTOR, "[class='sc-93ec7147-3 fUVkzh']").text
    assert f'{amount} item' in cart_sum

@then('Verify cart has correct product')
def verify_cart_has_correct_product(context):
    actual_results = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    print(actual_results)


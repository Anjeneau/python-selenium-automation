from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    VIEW_CART_CHECK_OUT = (By.XPATH, "//a[text()='View cart & check out']")
    SIDE_MENU_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    CART_SUM = (By.CSS_SELECTOR, "[class='sc-93ec7147-3 fUVkzh']")
    ACTUAL_NAME = (By.CSS_SELECTOR, "[data-test*='cartItem']")

    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_TXT)

    def view_cart_checkout(self):
        self.click(*self.VIEW_CART_CHECK_OUT)

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def confirm_add_to_cart(self):
        self.click(*self.SIDE_MENU_ADD_TO_CART)

    def verify_cart_item_amount(self, amount):
        self.get_text(*self.CART_SUM)

    def verify_correct_product(self):
        self.get_text(*self.ACTUAL_NAME)


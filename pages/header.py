from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_BTN = (By.XPATH, "//span[text()='Sign in']")
    SIDE_MENU_SIGNIN_BTN = (By.XPATH,"//a[@data-test='accountNav-signIn']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load

    def click_cart(self):
        self.wait_to_be_clickable_click(*self.CART_BTN)
        # self.driver.find_element(*self.CART_BTN).click()

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)

    def side_menu_signin(self):
        self.click(*self.SIDE_MENU_SIGNIN_BTN)

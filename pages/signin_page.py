from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE = (By.ID, "username")
    TTC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")
    TPP_LINK = (By.XPATH, "//a[text()='Target privacy policy']")

    def open_signin_page(self):
        self.open('https://www.target.com/account')

    def click_ttc_link(self):
        self.wait_to_be_clickable_click(*self.TTC_LINK)

    def verify_ttc_opened(self):
        self.verify_partial_url('terms-conditions/')



    def verify_signin_form(self):
        self.find_element(*self.SIGN_IN_PAGE)

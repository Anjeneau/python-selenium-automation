from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE = (By.ID, 'username')
    SIGNIN_BTN = (By.ID, 'login')
    ENTER_PASSWORD = (By.ID, 'password')
    NO_ACCT_MSG = (By.CSS_SELECTOR, "[data-test='authAlertDisplay']")
    TTC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")
    TPP_LINK = (By.XPATH, "//a[text()='Target privacy policy']")

    def open_signin_page(self):
        self.open('https://www.target.com/account')

    def enter_email_phone(self, info):
        self.input_text(info, *self.SIGN_IN_PAGE)

    def enter_password(self, info):
        self.input_text(info, *self.ENTER_PASSWORD)

    def click_signin_button(self):
        self.click(*self.SIGNIN_BTN)

    def click_ttc_link(self):
        self.wait_to_be_clickable_click(*self.TTC_LINK)

    def verify_no_account_message(self):
        self.find_element(*self.NO_ACCT_MSG)

    def verify_ttc_opened(self):
        self.verify_partial_url('terms-conditions/')

    def verify_signin_form(self):
        self.find_element(*self.SIGN_IN_PAGE)

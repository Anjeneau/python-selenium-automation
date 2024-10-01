from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE = (By.ID, "username")

    def verify_signin_form(self):
        self.find_element(*self.SIGN_IN_PAGE)

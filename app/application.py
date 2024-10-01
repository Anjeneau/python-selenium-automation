from pages.base_page import Page
from pages.header import Header
from pages.signin_page import SignInPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.signin_page = SignInPage(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
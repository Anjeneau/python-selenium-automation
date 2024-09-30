from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

@when('Search for {item}')
def search_item(context, item):
    #context.driver.find_element(By.ID, "search").send_keys(item)
    #context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    context.app.header.search_product(item)
    sleep(7)
# my computer can runs test extremely slow with explicit wait


@then('Verify search results correct for {item}')
def verify_result(context, item):
    #search_results = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']" ).text
    #assert item in search_results, f'Expected {item}, got {search_results}'
    context.app.search_results_page.verify_results(item)

@then('Verify product {item} in URL')
def verify_results_url(context, item):
    context.app.search_results_page.verify_results_url(item)



@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)
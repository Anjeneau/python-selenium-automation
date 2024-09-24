from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Search for {item}')
def search_item(context, item):
    print(item)
    context.driver.find_element(By.ID, "search").send_keys(item)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)


@then('Verify search results correct for {item}')
def verify_result(context, item):
    search_results = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']" ).text
    assert item in search_results, f'Expected {item}, got {search_results}'




from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

HELP_BUTTON = (By.XPATH, "//li[@class='nav_last']/a[contains(@href, 'gp/help/customer')]")
HELP_SEARCH = (By.XPATH, "//input[@id='helpsearch']")
GO_BUTTON_HELP_PAGE = (By.XPATH, "//input[@aria-labelledby='helpSearchSubmit-announce']")
HELP_CONTENT = (By.XPATH, "//div[@class='help-content']")


@when('Click Help button')
def click_help_button(context):
    context.driver.find_element(*HELP_BUTTON).click

@when('Input Cancel Order into search field')
def search_for_solution(context):
    context.driver.find_element(*HELP_SEARCH).clear()
    context.driver.find_element(*HELP_SEARCH).send_keys('Cancel Order')


'''@when('Input {help_request} into the search field')
def search_for_solution(context, help_request):
    # find "Search" field on the "help" paige, clear the field and input "Cancel Order"
    # search =
    context.driver.find_element(*HELP_SEARCH).clear()
    # search.clear()
    context.driver.find_element(*HELP_SEARCH).send_keys(help_request)
'''

sleep(4)

@when('Click Go button on the Help page')
def click_go_button_help_page(context):
    context.driver.find_element(*GO_BUTTON_HELP_PAGE).click()
    # find "Go" Button on the main paige and click on it

sleep(4)

@then('{help_search_result} text is in results')
def verify_help_search_result(context, help_search_result):
    # help_request_text = context.driver.find_element(*HELP_CONTENT).text
    assert help_search_result in context.driver.find_element(*HELP_CONTENT).text


from behave import then, when
from selenium.webdriver.common.by import By

TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
PRODUCT_BUTTON = (By.CSS_SELECTOR, "div.s-image-square-aspect")

@then('Search results for {product} is shown')
def verify_result(context, product):
    result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    assert product in result_text, f"Expected text is {product}, but got {result_text}"

@when ('Open the first product search result')
def open_first_product(context):
    context.driver.find_element(*PRODUCT_BUTTON).click()




'''
TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
PRODUCT_RESULTS = (By.XPATH, "//li[@role='listitem']//a[.//span[@class='a-price']]")


@when ('Open the firts product search result')
def click_first_result(context):
    context.driver.find_element(*PRODUCT_RESULTS).click()


@then ('Search results for {product} is shown')
def verify_result(context, product):
    result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    assert product == 'dress', f"Expected text is dress, but got {result_text}"
    '''
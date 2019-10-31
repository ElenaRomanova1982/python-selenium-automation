from behave import then, when
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART_TODAYS_DEALS = (By.CSS_SELECTOR, "button[aria-label*='Add to Cart']")





@when ('Click Add to cart button todays deals')
def click_add_to_cart_todays_deals(context):
    context.driver.find_element(*ADD_TO_CART_TODAYS_DEALS).click()
sleep(10)

@when ('Go back to the previous window and refresh')
def go_back_to_previous_window_and_refresh(context):
    context.driver.back()
    context.driver.refresh()
sleep(10)



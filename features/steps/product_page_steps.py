from behave import then, when
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CLOSING_X_SIDE_SELECTION = (By.ID, 'attach-close_sideSheet-link')

@when ('Click Add to cart button')
def open_amazon(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()

@when('Close suggestion side selection')
def close_side_suggestion(context):
    context.driver.find_element(*CLOSING_X_SIDE_SELECTION).click()

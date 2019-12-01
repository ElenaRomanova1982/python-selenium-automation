from behave import then, when
from selenium.webdriver.common.by import By
from time import sleep

PRIME_BENEFITS_CARDS = (By.CSS_SELECTOR, "div.card-clickable")


@then('{expected_number} cards represented Prime benefits are present')
def verify_number_of_cards(context, expected_number):
    sleep(3)
    actual_number = len(context.driver.find_elements(*PRIME_BENEFITS_CARDS))
    print(actual_number)
    assert actual_number == int(expected_number), \
        f'Expected {expected_number} items but got {actual_number}'

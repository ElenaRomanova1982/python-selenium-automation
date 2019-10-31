from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
#HAM_MENU = (By.ID, 'nav-hamburger-menu1')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULT = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button")
TODAYS_DEALS = (By.CSS_SELECTOR, "#nav-xshop > a[href*=goldbox]")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(4)

@when('Click Amazon Orders link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()


@when('Search for {product}')
def search_product(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on hamburger menu')
def click_ham_menu(context):
    context.driver.find_element(*HAM_MENU).click()

@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()

@when('Click on Todays deals button')
def click_todays_deals(context):
    context.driver.find_element(*TODAYS_DEALS).click()


@then('Verify cart has {expected_item_count} item')
def verify_item_count(context, expected_item_count):
    sleep(3)
    actual_items = context.driver.find_element(*CARD_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected{expected_item_count}, but got {actual_items}'

@then('6 menu items are present')
def verify_amount_of_items(context):
    sleep(3)
    print(len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULT)))
    assert len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULT)) == 6, \
        f'Expected 6 items but got {context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULT)}'

'''@then('Verify that hamburger menu is present')
def verify_ham_menu(context):
    sleep(3)
    context.driver.find_element(*HAM_MENU)'''

@then('Verify that hamburger menu is present')
def verify_ham_menu(context):
    print('\nFIND ELEMENTSSS =>> ')
    print(context.driver.find_elements(*HAM_MENU))
    print(type(context.driver.find_elements(*HAM_MENU)))

    print('\nFIND ELEMENT =>> ')
    print(context.driver.find_element(*HAM_MENU))
    print(type(context.driver.find_element(*HAM_MENU)))

from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CART_ITEM_COUNT = (By.ID, 'nav-cart-count')
CART_BUTTON_CHECK = (By.ID, 'nav-cart')
PRODUCT_IN_CART = (By.XPATH, "//span[@class='a-size-medium sc-product-title a-text-bold']")
HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")
TODAYS_DEALS = (By.CSS_SELECTOR, "#nav-xshop > a[href*=goldbox]")
TRY_PRIME_BUTTON = (By.CSS_SELECTOR, "a.nav-prime-try")


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

@when('Click on hamburger menu1')
def click_ham_menu1(context):
    context.driver.find_element(*HAM_MENU).click()

@when('Click onAmazon Music link1')
def click_amazon_music1(context):
    context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()
    sleep(4)

@then('6 menu items are present1')
def verify_amount_of_items1(context):
    print(len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)))
    assert len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)) == 6, f'Expected 6 items but got {len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))}'

@when('Click on Try Prime button')
def click_try_prime(context):
    context.driver.find_element(*TRY_PRIME_BUTTON).click()
    sleep(4)









'''@when('Search for {product}')
def search_product(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()'''


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
    actual_items = context.driver.find_element(*CART_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected{expected_item_count}, but got {actual_items}'

@then('Verify {product} in the cart')
def verify_product_added(context, product):
    context.driver.find_element(*CART_BUTTON_CHECK).click()
    sleep(3)
    product_text = context.driver.find_element(*PRODUCT_IN_CART).text
    assert product in product_text, f"Expected text is {product}, but got {product_text}"

    #result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    #assert product in result_text, f"Expected text is {product}, but got {result_text}"

@then('6 menu items are present')
def verify_amount_of_items(context):
    sleep(3)
    print(len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)))
    assert len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)) == 6, \
        f'Expected 6 items but got {context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)}'

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

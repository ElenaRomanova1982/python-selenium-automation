from behave import given, when, then
from selenium.webdriver.common.by import By

PRODUCTS = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div//li[.//div[contains(@class, 'brand-name')]]")
PRODUCT_NAME =(By.CSS_SELECTOR,'span.wfm-sales-item-card__product-name')
REGULAR = (By.CSS_SELECTOR, "span.wfm-sales-item-card__regular-price")

@given('Open Wholeffods Deals page')
def open_wholefoods_deals(context):
    context.driver.get("http://www.amazon.com/wholefoodsdeals")

@then('Each product has a regular price and a name')
def verify_regular_price(context):
    product_elements = context.driver.find_elements(*PRODUCTS)

    for product_element in product_elements:
        regular_price = product_element.find_element(*REGULAR).text
        print('\n', regular_price)
        assert '' != regular_price, f'Expected regular price is present in each product'
        print(len(context.driver.find_elements(*REGULAR)))

        #assert 'Regular' in product_element.text, f'Expected Regular to be in {product_element.text}'

        product_name = product_element.find_element(*PRODUCT_NAME).text
        print('\n',product_name)
        assert '' != product_name, f'Expected non-empty product name'
        print(len(context.driver.find_elements(*PRODUCT_NAME)))
        #count = product_elements.count(product_name)
        #print('\n','The count of products on the page is:', count)

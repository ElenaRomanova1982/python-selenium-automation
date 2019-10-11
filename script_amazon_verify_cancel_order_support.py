from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# init driver
# driver: WebDriver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
# open the url
driver.get('https://www.amazon.com/')

sleep(3)

# find "Help" Button on the main paige and click on it
driver.find_element(By.XPATH, '//li[@class=\'nav_last\']/a[contains(@href, \'gp/help/customer\')]').click()

sleep(3)

# find "Search" field on the "help" paige, clear the field and input "Cancel Order"
search = driver.find_element(By.XPATH, "//input[@id='helpsearch']")
search.clear()
search.send_keys('Cancel Order')

# wait for 4 sec
sleep(4)

# find "Go" Button on the main paige and click on it
driver.find_element(By.XPATH, "//input[@aria-labelledby='helpSearchSubmit-announce']").click()

# wait for 4 sec
sleep(4)

# verify
# assert 'Cancel Order' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert "Cancel Items or Orders" in driver.find_element(By.XPATH, '//div[@class=\'help-content\']').text
# assert "Cancel+Order&search" in driver.current_url

# wait for 4 sec
sleep(4)

driver.quit()

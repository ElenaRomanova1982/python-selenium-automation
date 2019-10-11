""" Locators Amazon Sign In Page"""

""" locator for Amazon Logo:  
   $x("//i[@class='a-icon a-icon-logo']");  driver.find_element_by_xpath("//i[@class='a-icon a-icon-logo']")"""

""" locator for Continue button: 
   $$("input[id=continue]") or  driver.findElement(By.id("continue")"""

"""locator for Need help link: 
   $x("//span[@class='a-expander-prompt']");  driver.find_element_by_xpath("//span[@class='a-expander-prompt']")  """

'''Forgot your password link:
   driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
   sleep(3)
   driver.findElement(By.id("auth-fpp-link-bottom") or driver.find_element(By.css("a[id=auth-fpp-link-bottom]")
'''

'''Other issues with Sign-In link:
   driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
   sleep(3)
   driver.findElement(By.id("ap-other-signin-issues-link") or driver.find_element(By.css("a[id=ap-other-signin-issues-link]")
'''

'''Create your Amazon account button:
$$("a[id=createAccountSubmit]")
driver.findElement(By.id("createAccountSubmit") 
or 
driver.find_element(By.css("a[id=createAccountSubmit]")
'''

'''Conditions of use link:
$x("//a[contains(@href, 'condition_of_use')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")
'''

'''Privacy Notice link:
$x("//a[contains(@href, 'notification_privacy_notice')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'notification_privacy_notice')]")
'''
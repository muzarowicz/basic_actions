driver.find_element_by_xpath("(//*[@class='list-menu-element -t-option-download ng-scope'])[2]").click() # click on second item
webdriver.find_element_by_xpath("(//*[@class='list-element-text more -t-more-options'])[position()=2]").click() # click on second item



'''unicode


#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''

#phantomJS
from selenium.webdriver import PhantomJS # pozniej zdefiniowac mozna stalo driver = PhantomJS()



"""
for i in range(100):
    email_address = "money" + str(i) + "@qa.test"
    firstName.send_keys("mike")
    lastName.send_keys("mano")
    emailField.send_keys(email_address)
    passwordField.send_keys("test12")
    submitButton.click()
"""



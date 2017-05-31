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
"""
#click on the text
    webdriver.find_element_by_xpath("//*[contains(text(), 'Ogłoszenia - Sprzedam, kupię na OLX.pl')]").click()
"""


"""
#oczekiwanie na element
WebElement myDynamicElement = (new WebDriverWait(driver, 10))
  .until(ExpectedConditions.presenceOfElementLocated(By.id("login")));

#sprawdzenie czy elem jest klikalny
WebDriverWait wait = new WebDriverWait(driver, 10);
WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.id("submit")));

###############################
hover elements

from selenium.webdriver.common.action_chains import ActionChains


def hover(self):
    wd = webdriver_connection.connection
    element = wd.find_element_by_link_text(self.locator)
    hov = ActionChains(wd).move_to_element(element)
    hov.perform()

next solution


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

firefox = webdriver.Firefox()
firefox.get('http://foo.bar')
element_to_hover_over = firefox.find_element_by_id("baz")

hover = ActionChains(firefox).move_to_element(element_to_hover_over)
hover.perform()

"""


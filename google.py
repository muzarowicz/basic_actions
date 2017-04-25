from selenium import webdriver
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

options = webdriver.ChromeOptions()
options.add_argument('--lang=es')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)

"""
driver.get("http://google.com")
url = driver.current_url
print (url)
driver.close()
"""

driver.get('https://www.olx.pl/')
driver.find_element_by_id('headerSearch').send_keys('huyndai i40')
driver.find_element_by_id('cityField').send_keys('Opole')
parentElement = driver.find_element_by_xpath("(//*[@class='tdnone title block c000 brtop-5 nowrap search-choose geo-suggest-row'])")
elementList = parentElement.find_element_by_tag_name('li')
url = driver.current_url
print (url)
print (elementList)
driver.find_element_by_xpath("(//*[@class='tdnone title block c000 brtop-5 nowrap search-choose geo-suggest-row'])[position()=2]").click()  # click on second item
driver.find_element_by_xpath("//input[@id='submit-searchmain']").click()
assert "zapytania." in driver.find_element_by_xpath("//*[@id='body-container']/div[2]/div/div[2]/p").text
driver.close()
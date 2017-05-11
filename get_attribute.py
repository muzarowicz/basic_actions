from selenium.webdriver import Chrome
import pytest
#from selenium import webdriver
driver = Chrome()
#driver = webdriver.PhantomJS()


def test_google():
    #driver = webdriver.PhantomJS("/usr/bin/phantomjs")
    #driver = webdriver.Chrome()
    driver.get("https://www.google.pl/")
    url = driver.current_url
    print (url)
    assert url == 'https://www.google.pl/'
def test_click():
    lst = driver.find_element_by_xpath("//input[@id='lst-ib']")
    val = lst.get_attribute("title")
    print (val)
    driver.close()
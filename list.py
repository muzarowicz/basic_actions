#!/usr/bin/env python
#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import Chrome
import os
import pytest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('download.default_directory=path_to_folder') #sciezka do folderu
path = "path_to_folder" # mozna dodac sciezke do folderu download


@pytest.fixture(scope='session')
def webdriver():
    driver = Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)
    return driver
"""
    # def test_download(webdriver):
    # Download the file using Selenium here
    before = os.listdir(path)
    print(before)
    webdriver.get('link_to_page')
    webdriver.find_element_by_xpath(
        "link_to_file").click()
    time.sleep(5)
    after = os.listdir(path)
    print (after)
    change = set(after) - set(before)
    print (change)
    if len(change) == 1:
        filename = change.pop()  # file name stored as string
        print(filename)
        os.remove(path+filename) # cala sciezka musi byc dodana po zlaczeniu path+filename jest git
    else:
        print "More than one file or no file downloaded"
"""
def test_list(webdriver):
    webdriver.get('https://www.olx.pl/')
    webdriver.find_element_by_id('headerSearch').send_keys('huyndai i40')
    time.sleep(2)
    webdriver.find_element_by_id('cityField').send_keys('Opole')
    time.sleep(2)
    parentElement = webdriver.find_element_by_id('autosuggest-geo-ul')
    elementList = parentElement.find_element_by_tag_name("li")
    url = webdriver.current_url
    print (url)
    print (elementList)
    webdriver.find_element_by_xpath("(//*[@class='tdnone title block c000 brtop-5 nowrap search-choose geo-suggest-row'])[position()=2]").click()  # click on second item
    webdriver.find_element_by_xpath("//input[@id='submit-searchmain']").click()
    #time.sleep(10)
    assert "Nie znaleźliśmy ogłoszeń dla tego zapytania." in webdriver.find_element_by_xpath("//*[@id='body-container']/div[2]/div/div[2]/p").text
    webdriver.close()
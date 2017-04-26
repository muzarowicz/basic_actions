#!/usr/bin/env python
#-*- coding: utf-8 -*-
from selenium.webdriver import PhantomJS
#from selenium.webdriver import Chrome
import os
import pytest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#options = webdriver.ChromeOptions()
#options.add_argument('--start-maximized')
#options.add_argument('download.default_directory=path_to_folder') #sciezka do folderu
path = "/home/mateusz/Downloads/" # mozna dodac sciezke do folderu download


@pytest.fixture(scope='session')
def webdriver():
    #driver = Chrome()
    #driver = Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)
    driver = PhantomJS()
    return driver
def test_download(webdriver):
    # Download the file using Selenium here
    before = os.listdir('/home/mateusz/Downloads')
    print(before)
    webdriver.get('https://support.spatialkey.com/spatialkey-sample-csv-data/')
    webdriver.find_element_by_xpath(
        "//*[@id='post-69']/div/h5[2]/a").click()
    time.sleep(5)
    after = os.listdir('/home/mateusz/Downloads')
    print (after)
    change = set(after) - set(before)
    print (change)
    if len(change) == 1:
        filename = change.pop()  # file name stored as string
        print(filename)
        os.remove(path+filename) # cala sciezka musi byc dodana po zlaczeniu path+filename jest git
    else:
        print "More than one file or no file downloaded"
        webdriver.close()

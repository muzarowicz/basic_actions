"""Test
prosta petla while - 4 krotne wykonanie testu
random choice """
import pytest
import random
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--start-maximized')
options.add_argument('--applicationCacheEnabled')
options.add_argument('--acceptSslCerts')



@pytest.fixture()
def webdriver(request):
    driver = Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)
    return driver


def test_title(webdriver):
    webdriver.get("https://www.google.com")
    assert 'Google' in webdriver.title


def test_fill(webdriver):
    count = 1
    while (count < 4):
        webdriver.get("https://www.google.com")
        # assert 'Google' in webdriver.title
        #webdriver.find_element_by_id('lst-bi').clear()
        webdriver.find_element_by_id('lst-ib').send_keys('hello')
        webdriver.find_element_by_id('lst-ib').send_keys(u'\ue007')
        time.sleep(4)
        assert webdriver.title == 'hello - Szukaj w Google' # poprawnie
        #assert 'hello - Szukaj w Google' in webdriver.title # poprawnie
        count = count + 1


def test_random(webdriver):
    myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
    webdriver.get("https://www.google.com")
    webdriver.find_element_by_id('lst-ib').send_keys(random.choice(myList))
    webdriver.find_element_by_id('lst-ib').send_keys(u'\ue007')
    print(random.choice(myList))

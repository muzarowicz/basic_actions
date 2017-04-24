from selenium.webdriver import Chrome
import pytest
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture(scope='session')
def webdriver():
    driver = Chrome()  # jesli nie chcesz uzywac parametryzacji przegladarki uzyj tej linijki
    return driver


"""do funkcji is_displayed"""

def test_element_visible(webdriver):
    webdriver.get("https://www.google.com")
    assert 'Google' in webdriver.title
    #assert webdriver.find_element_by_id('lst-ib')

def test_find(webdriver):
    if webdriver.find_element_by_id('lst-ib').is_displayed():
        webdriver.find_element_by_id('lst-ib').send_keys("hello")
        webdriver.find_element_by_id('lst-ib').send_keys(u'\ue007')
        time.sleep(4)
        assert 'hello - Szukaj w Google' in webdriver.title
    elif webdriver.find_element_by_id('email').is_displayed():
        print ("done")
    else:
        #webdriver.find_element_by_id('lst-ib').is_displayed()
        webdriver.get("https://www.google.com")
        webdriver.find_element_by_id('lst-ib').send_keys("hello")
        assert 'Google' in webdriver.title
        webdriver.close()

webdriver
"""funkcja try"""

def test_google(webdriver):
    webdriver.get("https://www.twitter.com")
    assert 'Twitter' in webdriver.title

def test_facebook(webdriver):
    found = False
    while found:
        try:
            webdriver.find_element_by_id('email')
            found = True
        except NoSuchElementException:
            time.sleep(2)
        try:
            webdriver.find_element_by_id('pass')
            found = True
        except NoSuchElementException:
            time.sleep(2)
    while found:
        try:
            webdriver.find_element_by_id('signin-email')
            found = False
        except Exception:
            time.sleep(2)
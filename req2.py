from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import requests
import pytest
import urllib

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')


@pytest.fixture(scope='session')
def webdriver():
    driver = Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)
    #request.addfinalizer(driver.quit)
    return driver

def test_nix_website_title(webdriver):
    webdriver.get('https://www.olx.pl')
    assert ' ' in webdriver.title

def test_go_to_POST(webdriver):
    webdriver.find_element_by_xpath("//a[@href='https://www.olx.pl/motoryzacja/']").click()
    WebDriverWait(webdriver, 10).until(lambda driver: webdriver.find_element_by_xpath("//a[@href='https://www.olx.pl/motoryzacja/samochody/']")).click()
    assert 'da' in webdriver.title

def test_response_POST(webdriver):
    WebDriverWait(webdriver, 10).until(lambda driver: webdriver.find_element_by_id('search-submit')).click()
    payload = {'category_id': 84, 'dist': 0, 'district_id': 0, 'filter_float_price': 35000}
    responsepost = requests.post('https://www.olx.pl/ajax/search/list/', data=payload)
    print(responsepost.status_code)
    print (responsepost.url)
    print(responsepost.text)
    webdriver.close()
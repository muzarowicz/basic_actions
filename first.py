import pytest
from selenium.webdriver import Chrome

@pytest.fixture(scope='session')
def webdriver(request):
    driver = Chrome()
    request.addfinalizer(driver.quit)
    return driver

def test_nix_website_title(webdriver):
    webdriver.get('https://github.com')
    assert 'GitHub' in webdriver.title

def test_pytest_website_title(webdriver):
    webdriver.get('https://twitter.com/?lang=en')
    assert 'Twitter' in webdriver.title
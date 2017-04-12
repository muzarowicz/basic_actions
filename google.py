from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--lang=es')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)


driver.get("http://google.com")

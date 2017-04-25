from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://google.com")
url = driver.current_url
print (url)
lst = driver.find_element_by_id('lst-ib')
val = lst.get_attribute("title")
print (val)
driver.close()

#rom seleniumrequests import Chrome
import requests

response = requests.get('http://google.com/')
print(response.status_code)
if response.status_code == 200:
    print('OK')
else:
    print('NOT OK')

#print(response.content)
print (response.url)
print (response.headers)

"""
webdriver.get("https://www.olx.pl/motoryzacja/samochody/")

def test_responsePOST():
    responsePOST = webdriver.request('POST', 'http://www.olx.pl/ajax/search/list/', data={"filter_float_price_from": "4000"})
    print(responsePOST)
    webdriver.close()
"""
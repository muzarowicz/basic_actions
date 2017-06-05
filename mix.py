""""Test prosta petla while - 4 krotne wykonanie testu
random choice
plus akcje z xlsx """

#from selenium import webdriver
import xlrd
import xlwt
import os.path
import pytest
import random
import time
import csv
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


@pytest.fixture(scope='session')
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



def test_csv():
    wb = xlwt.Workbook(encoding="utf-8")
    ws1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True) # 'cell_overwrite_ok=True ' aby mozna bylo nadpisywac
    ws2 = wb.add_sheet('Sheet 2',cell_overwrite_ok=True)
    ws3 = wb.add_sheet('Sheet 3',cell_overwrite_ok=True)

    ws1.row(0).write(0, 'Data written in first cell of first sheet')

    ws1.write(0, 0, 'Data overwritten in the first cell of first sheet')
    ws2.write(0, 0, 'Data written in first cell of second sheet')
    ws3.write(0, 0, 'Data written in first cell of third sheet')

    ws1.write(0, 1, 'Data written in first row,second column of first sheet')

    ws1.row(1).write(1, 'Data written in second row,second column of first sheet')

    var = "Data from variable written in third row,second column of first sheet"

    ws1.row(2).write(1,var)

    wb.save('/home/mateusz/Desktop/test_excel.xlsx')

    ws1.write(0, 0, '') #pusta cell

    wb.save('/home/mateusz/Desktop/test_excel.xlsx')

    na = xlrd.open_workbook(os.path.join('/home/mateusz/Desktop/test_excel.xlsx'))
    na.sheet_names()
"""
def test_csvReader(webdriver):
    #Read a csv file

    reader = csv.reader(webdriver)
    for row in reader:
        print(", ".join(row))

if __name__ == "__main__":
    csv_path = "/home/mateusz/Desktop/ada.csv"
    with open(csv_path, "rb") as f_obj:
        test_csvReader(f_obj)
"""
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
#----------------------------------------------------------------------
if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    path = "/home/mateusz/Desktop/output.csv"
    csv_writer(data, path)
#from selenium import webdriver
import xlrd
import xlwt
import pytest

@pytest.fixture()
def setup(request):
    wb = xlwt.Workbook(encoding="utf-8")
    ws1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True)
    ws2 = wb.add_sheet('Sheet 2',cell_overwrite_ok=True)
    ws3 = wb.add_sheet('Sheet 3',cell_overwrite_ok=True)
    return wb, ws1, ws2, ws3

def test_overwritten(setup):
    obj = setup()
    obj.ws1.row(0).write(0, 'Data written in first cell of first sheet')
    obj.ws1.write(0, 0, 'Data overwritten in the first cell of first sheet')
    obj.ws2.write(0, 0, 'Data written in first cell of second sheet')
    obj.ws3.write(0, 0, 'Data written in first cell of third sheet')

    obj.sws1.write(0, 1, 'Data written in first row,second column of first sheet')

    obj.ws1.row(1).write(1, 'Data written in second row,second column of first sheet')

    var = "Data from variable written in third row,second column of first sheet"

    obj.ws1.row(2).write(1,var)

def test_saveFile(setup):
    wb = xlwt.Workbook(encoding="utf-8")
    wb.save('/home/mateusz/Desktop/test_excel.xlsx')
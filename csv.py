#from selenium import webdriver
import xlrd
import xlwt
import os.path

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
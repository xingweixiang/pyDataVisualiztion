import xlrd
from xlrd.xldate import XLDateAmbiguous

file = 'ch02-xlsxdata.xlsx'
#打开文件的工作簿
wb = xlrd.open_workbook(filename=file)
#根据名称找到工作表
ws = wb.sheet_by_name('Sheet1')

dataset = []
#根据行数(nrows)和列数(ncols)读取单元格的内容
for r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r, c).value)
        if ws.cell_type(r, c) == xlrd.XL_CELL_DATE:
            try:
                #print (ws.cell_type(r, c))
                from datetime import datetime
                date_value = xlrd.xldate_as_tuple(ws.cell(r, c).value, wb.datemode)
                print (datetime(*date_value))
            except XLDateAmbiguous as e:
                print (e)
    dataset.append(col)

from pprint import pprint

pprint(dataset)



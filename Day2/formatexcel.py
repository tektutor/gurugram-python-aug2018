from openpyxl import * 
from openpyxl.worksheet.write_only import WriteOnlyCell
from openpyxl.styles import Font

workBook = Workbook(write_only = True)
workSheet = workBook.create_sheet()

cell = WriteOnlyCell(workSheet,  value="Some data")
cell.font = Font(name='Arial', size=25)
workSheet.append( [cell, 2, None])
workBook.save('myexcel.xlsx')


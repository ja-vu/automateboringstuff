import os
import openpyxl

os.chdir('c:\\Workspace\\automateboringstuff\\documents')

workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook['Sheet1']
cell = sheet['A1']
print(cell.value)
print(sheet['B1'].value)
print(sheet['C1'].value)

for i in range(1,8):
    print(i, sheet.cell(row=i,column=2).value)
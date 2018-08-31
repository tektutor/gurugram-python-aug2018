from openpyxl import load_workbook
wb = load_workbook(filename='test.xlsx', read_only=True)
ws = wb.active

for row in ws.rows:
    for cell in row:
        print(cell.value)

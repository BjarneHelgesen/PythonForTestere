import win32com.client

def test_formulas(sheet):
    sheet.Cells(1, 1).Value = 10 # A1
    sheet.Cells(2, 1).Value = 17 # A2
    sheet.Cells(3, 1).formula = "=A1+A2"
    if sheet.Cells(3, 1).Value == 27:
        return "Passed"
    else:
        return "Failed"


excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True  


workbook = excel.Workbooks.Add()
sheet = workbook.Sheets(1) 

print (test_formulas(sheet))





#print (dir(sheet))

#print (dir(sheet.Cells(3, 1))) 
#print (dir (workbook ))




from openpyxl import Workbook

##008000 this is for green

wb = Workbook()
wb['Sheet'].title="Report of Automation"
sh1=wb.active
sh1['A1'].value="Name"
sh1['B1'].value="Status"
sh1['A2'].value="Python"
sh1['B2'].value="Active"
sh1['A3'].value="Java"
sh1['B3'].value="Active1"
wb.save("C:\\Users\\SivakarnaSatri\\Desktop\\Working\DataExtracted.xlsx")


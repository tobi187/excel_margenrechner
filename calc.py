from openpyxl import load_workbook

def calc_marge(file_name):

    wb = load_workbook(file_name, data_only=True)

    for index,sheet in enumerate(wb.worksheets):

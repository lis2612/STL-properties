import openpyxl

book=openpyxl.open('data.xlsx',read_only=True)
sheet1=book['Аэро']

def search_in_cells(search_text):
    for row in range(1,sheet1.max_row+1):
        if sheet1[row][0].value==search_text:
            for col in range(1,sheet1.max_column):
                print(sheet1[row][col].value,end=' ')
            print()

def menu_days
search_in_cells('ПТ')
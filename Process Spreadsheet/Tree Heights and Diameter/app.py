import openpyxl as xl
from random import random

filename = input("Input Name of The Excel File To Open: ") + ".xlsx"
saved_filename = input("Input Name You Want To Save This Excel File: ") + ".xlsx"
wb = xl.load_workbook(filename)
sheet = wb["Sheet1"]

height_header = "Height"
diameter_header = "Diameter"
serial_no_header = "S/N"


for column in range(1, 4):
    for row in range(1, 452):
        cell = sheet.cell
        cell_value = cell(row, column)
        serial_no = row - 1
        if column == 1 and row == 1:
            cell_value.value = serial_no_header
        elif column == 2 and row == 1:
            cell_value.value = height_header
        elif column == 3 and row == 1:
            cell_value.value = diameter_header
        else:
            random_number = random() * 100
            if column == 1:
                cell_value.value = serial_no
            elif column == 2:
                while True:
                    random_number = random() * 100
                    if random_number <= 23:
                        cell_value.value = random_number
                        break
            elif column == 3:
                while True:
                    random_number = random() * 100
                    if random_number <= 46:
                        cell_value.value = random_number
                        break

    wb.save(saved_filename)
print(f"{saved_filename} has been modified and saved successfully")






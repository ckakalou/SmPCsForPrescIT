# Created by Christine Kakalou on 31/10/2022
# Project: SmPCs for PrescIT
#

import sqlite3  # Import the SQLite3 module
import pandas as pd     # Import the Pandas module
import os
from openpyxl import Workbook
from openpyxl.styles import Font

medicationList = []
eparEMAdirectory = os.fsencode(r"C:\Users\ckakalou\PycharmProjects\Healie\Data\SmPCs")
for file in os.listdir(eparEMAdirectory):
     filename = os.fsdecode(file)
     medicationName = filename.split("-epar-product-information")[0]
     medicationList.append(medicationName)


workbook = Workbook()
worksheet = workbook.active
#smpcData = [["SoC", "ADE", "Frequency"]]
overviewData = [["medicationName", "tableFound", "typeOfTable", "jsonFormat"]]

for row in overviewData:
    worksheet.append(row)

for i, value in enumerate(medicationList, start=2):
    worksheet.cell(row=i, column=1, value=value)

font = Font(bold=True)
for row in worksheet['A1':'D1']:
    for cell in row:
        cell.font = font

workbook.save(r"Data\SmPCs\overview.xlsx")







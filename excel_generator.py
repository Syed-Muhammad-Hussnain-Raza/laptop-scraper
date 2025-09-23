"""
@ Author: Syed Muhammad Hussnain Raza
@ Date: September 23, 2025
@ Description: Reads the parsed product data from out/products.json and generates
               an Excel file (out/products.xlsx). Converts URLs into clickable hyperlinks.
@ Dependencies: pandas, json, os
@ Inputs: out/products.json
@ Outputs: out/products.xlsx
@ LastModified: September 24, 2025
"""

import os
import pandas as pd
import json
from openpyxl import load_workbook


# Ensure output folder exists
os.makedirs("out", exist_ok=True)

# Load the parsed JSON data
with open("out/products.json", "r", encoding="utf-8") as f:
    products_list = json.load(f)

# Convert list of dictionaries to a DataFrame
df = pd.DataFrame(products_list)

# Make Image URL clickable in Excel
df["Image URL"] = df["Image URL"].apply(lambda x: f'=HYPERLINK("{x}", "{x}")' if x else "")

# Save to Excel file inside 'out' folder
excel_file = "out/products.xlsx"
df.to_excel(excel_file, index=False)

# 🔹 Auto-fit column widths using openpyxl (Optional, Just save us from manual resizing of column width.)
wb = load_workbook(excel_file)
ws = wb.active
for col in ws.columns:
    max_length = 0
    col_letter = col[0].column_letter
    for cell in col:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))
    ws.column_dimensions[col_letter].width = max_length + 2
wb.save(excel_file)

print(f"✅ Excel file '{excel_file}' created successfully with clickable URLs!")

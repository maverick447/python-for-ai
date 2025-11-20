import pandas as pd
import json
import os

# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
print(f"Shape overall is: {df.shape}")
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")


# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

output_dir = 'output'
# Create output directory
os.makedirs(output_dir, exist_ok=True)

json_output_file = output_dir + '/' + 'sales_data.json'
print(json_output_file)
# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json(json_output_file, orient='records', indent=2)

# to read it back from json file  
df2 = pd.read_json(json_output_file) 
print(df2)
# JSON
# or for simple JSON:
with open(json_output_file, 'r') as f:
    data = json.load(f)
    print(data)

excel_output_file = output_dir + '/' + 'sales_data.xlsx'
print(excel_output_file)
# 2. Excel format (good for sharing)
df.to_excel(excel_output_file, index=False)

# Read from Excel
df3= pd.read_excel(excel_output_file)
print(df3)

# 3. Updated CSV (with our new total column)
excel_with_totals_file = output_dir + '/' + 'sales_data_with_totals.xlsx'
print(excel_with_totals_file)
df.to_excel(excel_with_totals_file, index=False)
# Read from Excel
df4 = pd.read_excel(excel_with_totals_file)
print(df4)

# 4 . plain text file 
txt_output_file = output_dir + '/' + 'sales_data_with_totals.txt'
print(txt_output_file)
# File out 
df.to_string(txt_output_file)
# File in 
# pandas 
# delim_whitespace is deprecated 
# df5 = pd.read_csv(txt_output_file,delim_whitespace=True)
df5 = pd.read_csv(txt_output_file, sep=r'\s+')
print(df5)
# if you use plain txt reading 


print("\nFiles saved:")
print(f"- {json_output_file}")
print(f"- {excel_output_file}") 
print(f"- {excel_with_totals_file}")
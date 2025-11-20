# analyzer.py
import pandas as pd

# from helpers import calculate_total, format_currency
import helpers as hp
import os

current_path = os.getcwd()
print("Current directory:", current_path)

if not os.path.exists("sales_analysis"):
    print("Error: 'sales_analysis' directory does not exist.")
    os.chdir(
        "/Volumes/Drive/code/Python/PythonProjects/python-for-ai/code/sales-analysis"
    )
    print("Changed directory to:", os.getcwd())
# Read data
df = pd.read_csv("data/sales.csv")
print(df)
# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = hp.calculate_total(row["quantity"], row["price"])
    totals.append(total)

# Add totals to our data
df["total"] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = hp.format_currency(row["total"])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df["total"].sum()
formatted_grand_total = hp.format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

# we can print the data to a new csv file
df[["product", "total"]].to_csv("sales_history_1.csv", index=False)  # Write CSV

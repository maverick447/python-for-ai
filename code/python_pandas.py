import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 25, 27],
    "City": ["Austin", "Dallas", "Houston"],
}

df = pd.DataFrame(data)
print(df)

df_original = df
# it writes to a file in CSV format
df.to_csv("batch_mates.csv", index=False)  # Write CSV

# read from a file
df = pd.read_csv("batch_mates.csv")
print(df)

# there is logic error here when we do print out the type of the variable --> <class 'pandas.core.frame.DataFrame'>
# basically what we need is a single boolean variable
# bool_both_in_and_out_are_same = (df_original == df)
bool_both_in_and_out_are_same = df_original.equals(df)
print(type(bool_both_in_and_out_are_same))


print(
    f"We are testing the values before and after and result is {bool_both_in_and_out_are_same}"
)


# writing to Excel
df.to_excel("batch_mates.xlsx", sheet_name="batch_mates")

# read from Excel
# Step 3: Read back from Excel
df_read = pd.read_excel("batch_mates.xlsx", sheet_name="batch_mates")
print("\n📖 Data read back from Excel:")
print(df_read)

# Step 2: Write to a JSON file
df.to_json("batch_mates.json", orient="records", indent=4)
print("\n✅ Data written to 'batch_mates.json'")

# Step 3: Read JSON back into a DataFrame
df_read = pd.read_json("batch_mates.json")
print("\n📖 Data read from JSON:")
print(df_read)

# first 5 rows
df.head()  # first 5 rows
df.info()  # data types and non-null info

data_cars = {
    "Name": ["Rolls-Royce", "Lamborghini", "Porsche"],
    "SpeedMph": [201, 215, 230],
    "CountryOrigin": ["England", "Germany", "Germany"],
    "Price": [444000.0, 500000.0, 250000],
}

df = pd.DataFrame(data_cars)
print(df)

# Selecting Specific data
print(df["Name"])
print(df[["Name", "Price"]])
df.iloc[0]

df.iloc[0, 2]

df.iloc[:, 0:4]
# df.iloc[[0, 0], [3,3]]
df.loc[2, "Name"]

# Adding a column
df["Type"] = ["Luxury", "Sports", "Sports"]
print(df)

# adding a row
df.loc[3] = ["Ferrari", 220, "Italy", 350000, "Sports"]
print(df)

print(df.loc[3])

df.loc[4] = ["Bentley", 210, "England", "370000", "Luxury"]
print(df)

# removing an element from a column
# df.drop("Type", axis =1, inplace=True)
# print(df)

# df.drop("Name", axis =1, inplace=True)
# print(df)

# beware all of data is destroyed
# df = df[0:0]
# print(df)

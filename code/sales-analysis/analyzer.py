import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
#data_path = "data/sales.csv"
# folders above the current path
data_path = "../data/austin_weather_2025-11-14_2025-11-21.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

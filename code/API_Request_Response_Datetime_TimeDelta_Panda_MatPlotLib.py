import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_next = today + timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = today.strftime("%Y-%m-%d")
end_date = week_next.strftime("%Y-%m-%d")

# Get Austin weather for past week
latitude = 30.2672
longitude = -97.7431
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=America/Chicago&temperature_unit=fahrenheit"
# print(url)
# url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
print(url)

response = requests.get(url)
data = response.json()
print(data)
# Extract the daily data
daily_data = data["daily"]
print(daily_data)

# Create a DataFrame
df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)

df["date"] = pd.to_datetime(df["date"])
print(df)

print(type(df["date"]))

# lets introduce mathplotlib
plt.figure(figsize=(10, 6))
"""
plt.plot(x, y, 
         marker='o',       # Marker at each data point
         color='red',      # Line color
         linestyle='-',   # Line style: '-', '--', ':', '-.'
         linewidth=2,      # Thickness of the line
         label='Max Temp') # Label for legend
"""
plt.plot(
    df["date"],
    df["max_temp"],
    marker=".",
    color="red",
    label="Max Temp",
    linestyle="-",
    linewidth=1,
)
plt.plot(
    df["date"],
    df["min_temp"],
    marker=".",
    color="#0090FF",
    label="Min Temp",
    linestyle="-",
    linewidth=1,
)
# plt.grid(True)
"""
plt.grid(True,       # Turn grid on
         which='major',  # Major ticks
         color='gray',   # Grid color
         linestyle='--', # Dashed lines
         linewidth=0.5)  # Line width
"""
plt.xlabel("Date")
plt.ylabel("Temperature (°F)")
plt.title("Austin Weather - Next 7 Days")
plt.legend()
# Rotate x-axis labels for readability
plt.xticks(rotation=45)
# automatically adjusts the spacing of your plot elements so that nothing overlaps — like titles, labels, tick labels, or legends.
plt.tight_layout()

# save the plot
plt.savefig("weather_for_week.png")
# finally show the plot
plt.show()

# save csv from df
if not os.path.exists("weatherdata"):
    os.makedirs("weatherdata")

name_of_file = f"weatherdata/austin_weather_{start_date}_{end_date}.csv"
df.to_csv(name_of_file)
print(f"WeatherData saved to csv file: {start_date}")

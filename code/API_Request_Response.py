import requests

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&timezone=America/Chicago&temperature_unit=fahrenheit"
    # Make the request
    response = requests.get(url)
    data = response.json()
    return data['current']['temperature_2m']

# Austin time 
austin_latitude = 30.2672
austin_longitude = -97.7431

austin_temp = get_weather(austin_latitude, austin_longitude)
print(f"Austin: {austin_temp}°F")

# New york 40.7580° N, 73.9855° W
ny_latitude = 40.7580
ny_longitude = 73.9855

ny_temp = get_weather(ny_latitude, ny_longitude)
print(f"New York: {ny_temp}°F")

# Downtown SF: 37.7749° N, 122.4194° W
sf_latitude = 37.7749
sf_longitude = 122.4194

sf_temp = get_weather(sf_latitude, sf_longitude)
print(f"San Francisco: {sf_temp}°F")

# Downtown Chicago (Loop): 41.8781° N, 87.6298° W
chicago_latitude = 41.8781
chicago_longitude = 87.6298

chicago_temp = get_weather(chicago_latitude, chicago_longitude)
print(f"Chicago: {chicago_temp}°F")


# # Build the API URL with our parameters

# print(data)

# print(type(data))
# print(type(data.keys()))
# print(data.keys())

# # aim is to get temperature 
# print(data["current"]['temperature_2m'])

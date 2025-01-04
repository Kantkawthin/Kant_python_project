import requests

# API key
api_key = 'ca7a84415dfba5467ecf2dbc3a81868c'

# Latitude and Longitude (ensure lat and lon are defined)
lat = 35.6895  # Example: Latitude of Tokyo
lon = 139.6917  # Example: Longitude of Tokyo

# Current weather API call
current_weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
current_weather_data = requests.get(current_weather_api).json()
print("Current Weather Data:")
print(current_weather_data)

# Daily forecast API call (use /forecast instead of /forecast/daily)
forecast_api = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt=7&appid={api_key}"
forecast_data = requests.get(forecast_api).json()
print("\nForecast Data:")
print(forecast_data)

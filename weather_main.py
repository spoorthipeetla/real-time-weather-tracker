import os
import requests
from dotenv import load_dotenv

# 1. Load the secret API key from the hidden .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    # The URL where OpenWeatherMap listens for requests
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # The data we are sending them
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" # This gets the temperature in Celsius
    }

    # 2. Make the request
    response = requests.get(base_url, params=params)

    # 3. Check if it worked (Status code 200 means OK)
    if response.status_code == 200:
        data = response.json()
        print(f"Success! We got the data for {city}:")
        print(data)
    else:
        print(f"Uh oh! Error: {response.status_code}")

# Let's test it out!
if __name__ == "__main__":
    get_weather("Madanapalle")
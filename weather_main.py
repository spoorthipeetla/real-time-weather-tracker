import os
import requests
from dotenv import load_dotenv
import streamlit as st  # 1. We imported our UI tool!
import base64
# Load the secret API key
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()  # 2. We return the data now instead of printing it
    else:
        return None

# --- STREAMLIT UI SECTION ---

# 3. Create a big title for your web page
st.title("🌦️ Live Weather Dashboard")

# 4. Create an input box where the user can type a city
city_input = st.text_input("Enter a city name:", "Madanapalle")

# 5. Create a button to trigger the search
if st.button("Get Weather"):

    # Fetch the data using our backend function
    weather_data = get_weather(city_input)

    # 6. Unpack the JSON and display it cleanly on the web!
    if weather_data:
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        condition = weather_data['weather'][0]['description'].capitalize()

        # st.metric is a special Streamlit tool for displaying numbers nicely
        st.metric(label=f"Temperature in {city_input}", value=f"{temp} °C")

        # st.write is how we put regular text on the web page
        st.write(f"**Feels like:** {feels_like} °C")
        st.write(f"**Conditions:** {condition}")
    else:
        st.error("Uh oh! Could not find that city. Check your spelling.")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 2. Tell Python EXACTLY where the image is using a raw string (the 'r' before the quotes)
# This stops Python from misinterpreting the backslashes
local_image_path = "bg.jpg"

# 3. Translate the image
base64_img = get_base64_of_bin_file(local_image_path)

# 4. Inject the translated text directly into the CSS
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("data:image/jpg;base64,{base64_img}");
background-size: cover;
background-position: center;
}}

[data-testid="stHeader"] {{
background-color: rgba(0,0,0,0);
}}
</style>
"""

# 5. Apply the CSS to the page
st.markdown(page_bg_img, unsafe_allow_html=True)
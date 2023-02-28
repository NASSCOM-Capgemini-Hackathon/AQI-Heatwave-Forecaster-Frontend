# Libraries
import pandas as pd
import requests
from utils import bargraph, linegraph, get_request_data, get_current_aqi
import numpy as np


# Data Sources
# @st.cache(ttl=1000, allow_output_mutation=True)


def get_data(query, city_name=None):
    if query == 'Transactions Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/579714e6-986e-421a-85dd-c32a8b41b25c/data/latest')
    elif query == "Get current data":

        api = "9b833c0ea6426b70902aa7a4b1da285c"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}"
        response = requests.get(url)
        x = response.json()

        weatherforecast_url = "https://aqi-heatwave-app.azurewebsites.net/api/weather/getDailyWeatherPredictions"
        df_weather = get_request_data(weatherforecast_url, cityname=city_name)
        df_weather['Predictions'] = np.round(df_weather['Predictions'], 2)

        aqiforecast_url = "https://aqi-heatwave-app.azurewebsites.net/api/aqi/getDailyAQIPredictions"
        df_aqi = get_request_data(aqiforecast_url, cityname=city_name)
        df_aqi['Predictions'] = np.round(df_aqi['Predictions'], 2)

        current_aqi = get_current_aqi(city_name)

        forecast_dates = df_weather['Date'].to_list()[:7]
        aqi_forecast = df_aqi['Predictions'].to_list()[:7]
        weather_forecast = df_weather['Predictions'].to_list()[:7]

        for i in range(len(forecast_dates)):
            date = pd.to_datetime(forecast_dates[i], format="%Y-%m-%d")
            date = date.day_name()
            forecast_dates[i] = date

        try:

            cel = 273.15
            icon = x["weather"][0]["icon"]
            current_weather = x["weather"][0]["description"].title()
            temp = str(round(x["main"]["temp"]-cel, 2))
            line_aqi_fig = linegraph(
                forecast_dates, aqi_forecast, "AQI", "DATES", "AQI")
            line_weather_fig = linegraph(
                forecast_dates, weather_forecast, "WEATHER", "DATES", "WEATHER")

            return line_aqi_fig, line_weather_fig, temp, current_weather, icon, forecast_dates, aqi_forecast, weather_forecast, current_aqi

        except Exception as e:
            print("Error message "+str(e))

    return None

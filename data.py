# Libraries
import pandas as pd
import datetime
import requests
from utils import bargraph, linegraph ,get_request_data
from pandas import json_normalize
import numpy as np
import json


# Data Sources
# @st.cache(ttl=1000, allow_output_mutation=True)


def get_data(query , city_name = None):
    if query == 'Transactions Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/579714e6-986e-421a-85dd-c32a8b41b25c/data/latest')
    elif query == "Get current data":
        temp_unit = " °C"
        wind_unit = " km/h"
        api = "9b833c0ea6426b70902aa7a4b1da285c"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}"
        response = requests.get(url)
        x = response.json()

        weatherforecast_url = "https://aqi-heatwave-app.azurewebsites.net/api/weather/getDailyWeatherPredictions"
        df_weather = get_request_data(weatherforecast_url,cityname=city_name)
        df_weather['Predictions']=np.round(df_weather['Predictions'],2)

        aqiforecast_url = "https://aqi-heatwave-app.azurewebsites.net/api/aqi/getDailyAQIPredictions"
        df_aqi = get_request_data(aqiforecast_url,cityname=city_name)
        df_aqi['Predictions']=np.round(df_aqi['Predictions'],2)

        date = df_weather['Date'].to_list()
        aqi_date = df_aqi['Date'].to_list()

        print(weather_date,aqi_date)


        try:
            lon = x["coord"]["lon"]
            lat = x["coord"]["lat"]
            ex = "current,minutely,hourly"
            url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={ex}&appid={api}'
            res = requests.get(url2)
            y = res.json()

            maxtemp = []
            mintemp = []
            pres = []
            humd = []
            wspeed = []
            desc = []
            cloud = []
            rain = []
            dates = []
            sunrise = []
            sunset = []
            cel = 273.15

            for item in y["daily"]:
                maxtemp.append(round(item["temp"]["max"]-cel, 2))
                mintemp.append(round(item["temp"]["min"]-cel, 2))
                wspeed.append(str(round(item["wind_speed"]*3.6, 1))+wind_unit)

                pres.append(item["pressure"])
                humd.append(str(item["humidity"])+' %')

                cloud.append(str(item["clouds"])+' %')
                rain.append(str(int(item["pop"]*100))+'%')

                desc.append(item["weather"][0]["description"].title())

                d1 = datetime.date.fromtimestamp(item["dt"])
                dates.append(d1.strftime('%d %b'))

                sunrise.append(datetime.datetime.utcfromtimestamp(
                    item["sunrise"]).strftime('%H:%M'))
                sunset.append(datetime.datetime.utcfromtimestamp(
                    item["sunset"]).strftime('%H:%M'))

            icon = x["weather"][0]["icon"]
            current_weather = x["weather"][0]["description"].title()

            temp = str(round(x["main"]["temp"]-cel, 2))

            bar_fig = bargraph(dates, maxtemp, "Maximum", "Dates",
                               "Temperature", mintemp, "Mininum")

            line_fig = linegraph(dates, maxtemp, "Maximum", "Dates",
                                 "Temperature", mintemp, "Mininum")

            df = pd.DataFrame({'DATES': dates,
                               'MAX TEMP '+temp_unit: maxtemp,
                               'MIN TEMP'+temp_unit: mintemp,
                               'HUMIDITY': humd,
                               'WEATHER CONDITION': desc,
                               'WIND SPEED': wspeed,
                               })

            return df, bar_fig, line_fig, temp, current_weather, icon

        except Exception as e:
            print("Error message "+str(e))

    return None

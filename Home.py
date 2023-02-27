# Libraries
import streamlit as st
from PIL import Image
import pandas as pd
import datetime
import requests
from plotly import graph_objects as go
from utils import bargraph, linegraph

# Confit
st.set_page_config(page_title='AQI Weather Forecaster',
                   page_icon=':bar_chart:', layout='wide', initial_sidebar_state='collapsed')

city = st.selectbox("SELECT ANY ONE OF THE CITY ", ("Adilabad",
                    "Nizamabad", "Khammam", "Warangal", "Karimnagar"))

graph = "Bar Graph"
temp_unit = " °C"
wind_unit = " km/h"


api = "9b833c0ea6426b70902aa7a4b1da285c"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
response = requests.get(url)
x = response.json()


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

    col1, col2 = st.columns(2)
    with col1:
        st.write("## Current Temperature ")
    with col2:
        st.image(
            f"http://openweathermap.org/img/wn/{icon}@2x.png", width=70)

    col1, col2 = st.columns(2)
    col1.metric("TEMPERATURE", temp+temp_unit)
    col2.metric("WEATHER", current_weather)

    tab1, tab2 = st.tabs(["Bar Graph", "Line Graph"])

    with tab1:
        st.plotly_chart(bargraph(dates, maxtemp, "Maximum", "Dates",
                        "Temperature", mintemp, "Mininum"), use_container_width=True)

    with tab2:
        st.plotly_chart(linegraph(dates, maxtemp, "Maximum", "Dates",
                        "Temperature", mintemp, "Mininum"), use_container_width=True)

    df = pd.DataFrame({'DATES': dates,
                       'MAX TEMP '+temp_unit: maxtemp,
                       'MIN TEMP'+temp_unit: mintemp,
                       'HUMIDITY': humd,
                       'WEATHER CONDITION': desc,
                       'WIND SPEED': wspeed,
                       })
    st.table(df)

except Exception as e:
    st.error("Error message "+e)

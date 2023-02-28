# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import requests
import json
import codecs
from pandas import json_normalize
import numpy as np
from streamlit_card import card
from datetime import date


# Global Variables
theme_plotly = "streamlit"  # None or streamlit


def get_aqi_message(aqi):
    if aqi <= 50:
        message = "Air quality is good ✅. Enjoy your outdoor activities!"
    elif aqi <= 100:
        message = "Air quality is moderate 🧐. People with respiratory issues may experience symptoms."
    elif aqi <= 150:
        message = "Air quality is unhealthy for sensitive groups 😶‍🌫️. Children, older adults and people with heart or lung disease should reduce prolonged or heavy exertion."
    elif aqi <= 200:
        message = "Air quality is unhealthy 😷. Everyone may experience symptoms."
    elif aqi <= 300:
        message = "Air quality is very unhealthy 😵. People with respiratory or heart disease, older adults, and children should avoid prolonged or heavy exertion."
    else:
        message = "Air quality is hazardous ☠️. Everyone should avoid outdoor activities."

    return message


def display_daily(city):

    # Define the API endpoint URL
    history_url = "https://aqi-heatwave-app.azurewebsites.net/api/weather/getHistoryDailyWeather"
    future_url = "https://aqi-heatwave-app.azurewebsites.net/api/weather/getDailyWeatherPredictions"

    # Define the request payload
    payload = {
        "City": city
    }

    # Send the POST request and store the response in a variable
    r1 = requests.post(history_url, json=payload)
    data1 = json.loads(r1.text)
    # Convert the response to a pandas DataFrame
    df_hist = json_normalize(data1)
    df_hist['Max '] = np.round(df_hist['AQI'])

    r2 = requests.post(future_url, json=payload)
    data2 = json.loads(r2.text)
    # Convert the response to a pandas DataFrame
    df_fut = json_normalize(data2)
    df_fut['Predictions'] = np.round(df_fut['Predictions'])

    with st.container():
        #st.title('CURRENT AIR QUALITY')
        st.markdown(
            "<h2 style='font-family:Times New Roman'><b>CURRENT AIR QUALITY INDEX</b></h2>", unsafe_allow_html=True)
        st.markdown("""---""")
        col1, col2, col3 = st.columns(3)

        today_date = str(date.today())
        st.write(today_date)

        today_aqi = df_hist.loc[df_hist['DATE'] == today_date, 'AQI'].values[0]
        with col1:
            st.header("**TODAY**")
            st.text(today_date)
        with col2:

            card(
                title="AQI",
                text=today_aqi,
                image='https://t3.ftcdn.net/jpg/01/70/53/70/240_F_170537095_942g7Zk2TcXplIdXpraxPN1C7YR8kDEk.jpg'

            )

        text = get_aqi_message(today_aqi)
        st.markdown(
            f"<h3 style='font-family:Times New Roman'>{text}</h3>", unsafe_allow_html=True)

        # st.write(hasClicked)

    st.write('')
    st.write('')
    with st.container():

        st.markdown(
            "<h2 style='font-family:Times New Roman'><b>DAILY AIR QUALITY INDEX FORECAST</b></h2>", unsafe_allow_html=True)
        st.markdown("""---""")

        fig = go.Figure(data=go.Bar(x=df_fut['Date'], y=df_fut['Predictions']))

        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='AQI'
        )
        st.plotly_chart(fig, use_container_width=True)


def display_monthly(city):
    history_url = "https://aqi-heatwave-app.azurewebsites.net/api/aqi/getHistoryMonthlyAQI"
    future_url = "https://aqi-heatwave-app.azurewebsites.net/api/aqi/getMonthlyAQIPredictions"

    # Define the request payload
    payload = {
        "City": city
    }

    # Send the POST request and store the response in a variable
    r1 = requests.post(history_url, json=payload)
    data1 = json.loads(r1.text)
    # Convert the response to a pandas DataFrame
    df_hist = json_normalize(data1)
    df_hist['Max Temp (°C)'] = np.round(df_hist['Max Temp (°C)'])

    r2 = requests.post(future_url, json=payload)
    data2 = json.loads(r2.text)
    # Convert the response to a pandas DataFrame
    df_fut = json_normalize(data2)
    df_fut['Predictions'] = np.round(df_fut['Predictions'])

    with st.container():
        st.markdown(
            "<h2 style='font-family:Times New Roman'><b>CURRENT AIR QUALITY INDEX</b></h2>", unsafe_allow_html=True)
        st.markdown("""---""")
        col1, col2, col3 = st.columns(3)

        today_date = date.today()
        res = today_date.replace(day=1)
        st.write(res)
        today_aqi = df_hist.loc[df_hist['DATE'] == res, 'AQI'].values[0]
        with col1:
            st.header("**TODAY**")
            st.text(today_date)
        with col2:

            card(
                title="AQI",
                text=today_aqi,
                image='https://t3.ftcdn.net/jpg/01/70/53/70/240_F_170537095_942g7Zk2TcXplIdXpraxPN1C7YR8kDEk.jpg'

            )

        text = get_aqi_message(today_aqi)
        st.markdown(
            f"<h3 style='font-family:Times New Roman'>{text}</h3>", unsafe_allow_html=True)

        # st.write(hasClicked)

    st.write('')
    st.write('')
    with st.container():
        st.markdown(
            "<h2 style='font-family:Times New Roman'><b>MONTHLY AIR QUALITY INDEX FORECAST</b></h2>", unsafe_allow_html=True)
        st.markdown("""---""")

        fig = go.Figure(data=go.Bar(x=df_fut['Date'], y=df_fut['Predictions']))

        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='AQI'
        )
        st.plotly_chart(fig, use_container_width=True)


# Config
st.set_page_config(page_title='Air Quality Index',
                   page_icon=':bar_chart:', layout='wide')
st.text("")
st.text("")
# Title

st.markdown("<h1 style='text-align: center; color: #D81F26; font-family:Times New Roman'><b>🏭 AIR QUALITY INDEX</b></h1>", unsafe_allow_html=True)
st.text(" ")
st.text(" ")
# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Data Sources

# Filter
options = st.sidebar.selectbox(
    "Select the Frequency for AQI",
    ("Daily", "Monthly")
)
city_list = ['Adilabad', 'Warangal', 'Karimnagar', 'Khammam', 'Nizamabad']
city = st.sidebar.selectbox(
    "Select City",
    city_list
)

if options == 'Daily':
    display_daily(city)
else:
    display_monthly(city)

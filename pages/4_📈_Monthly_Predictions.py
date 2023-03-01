# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import requests
import json
import codecs
import s3fs
from pandas import json_normalize
import numpy as np
from streamlit_card import card
from datetime import date
import utils
import prophet
from prophet.serialize import model_from_json
import warnings
warnings.filterwarnings("ignore")


def print_top3(df):
    col_list = list(st.columns(3, gap="medium"))
    for i in range(len(col_list)):
        with col_list[i]:
            # print(df['Predictions'].iloc[i])
            st.metric(pd.to_datetime(df['Date'].iloc[i]).strftime(
                '%B'), round(df['Predictions'].iloc[i], 2))


def get_statistics(df, feature):
    sorted_desc = df.sort_values('Predictions', ascending=False)
    st.header("Top 3 Months with highest {}".format(feature))
    print_top3(sorted_desc)
    sorted_asc = df.sort_values('Predictions', ascending=True)
    st.header("Top 3 Months with lowest {}".format(feature))
    print_top3(sorted_asc)


def display_aqi(city, slider_col):
    st.markdown("<hr>",
                unsafe_allow_html=True)
    st.header(city)

    fs = s3fs.S3FileSystem(key='AKIAQOY2QI5NU7SFAHPH',
                           secret='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')
    with fs.open('capegemini-hackathon/predictions/aqi/{}/aqi.csv'.format(city)) as f:
        aqi_city = pd.read_csv(f, header=0)

    aqi_city = aqi_city[aqi_city['Date'] < '2024-01-01']
    st.markdown("<hr>",
                unsafe_allow_html=True)
    st.text("")
    with slider_col:
        start_month, end_month = st.select_slider('Pick Month Range', options=(aqi_city['Date']), value=(
            aqi_city['Date'].iloc[0], aqi_city['Date'].iloc[-1]))
    aqi_city = aqi_city[(aqi_city['Date'] >=
                        start_month) & (aqi_city['Date'] <= end_month)]
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.table(aqi_city)
    with col2:
        st.subheader('{} Monthly Predictions'.format(city))
        fig = utils.linegraph(aqi_city['Date'],
                              aqi_city['Predictions'], 'AQI', 'Date', 'AQI')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    get_statistics(aqi_city, 'AQI')


def load_prophet(city):
    with open('models\{}_model.json'.format(city), 'r') as fin:
        m = model_from_json(fin.read())

    fs = s3fs.S3FileSystem(key='AKIAQOY2QI5NU7SFAHPH',
                           secret='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')
    with fs.open('capegemini-hackathon/prophet/forecasts/pred-{}.csv'.format(city)) as f:
        forecasts = pd.read_csv(f, header=0)
    forecasts.drop(list(forecasts.columns)[0], axis=1, inplace=True)
    fig1 = prophet.plot.plot_plotly(m, forecasts)
    st.plotly_chart(fig1, use_container_width=True)


def display_heatwave(city, slider_col):
    fs = s3fs.S3FileSystem(key='AKIAQOY2QI5NU7SFAHPH',
                           secret='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')
    with fs.open('capegemini-hackathon/predictions/weather/{}/weather.csv'.format(city)) as f:
        weather_city = pd.read_csv(f, header=0)
    weather_city = weather_city[(
        weather_city['Date'] < '2024-01-01') & (weather_city['Date'] > '2022-12-01')]
    st.markdown("<hr>",
                unsafe_allow_html=True)
    st.text("")
    with slider_col:
        start_month, end_month = st.select_slider('Pick Month Range', options=(weather_city['Date']), value=(
            weather_city['Date'].iloc[0], weather_city['Date'].iloc[-1]))
    weather_city = weather_city[(weather_city['Date'] >=
                                 start_month) & (weather_city['Date'] <= end_month)]
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.table(weather_city)
    with col2:
        st.subheader('{} Monthly Predictions'.format(city))
        fig = utils.linegraph(weather_city['Date'],
                              weather_city['Predictions'], 'AQI', 'Date', 'AQI')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    get_statistics(weather_city, 'Weather')
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Prophet Model Forecasts")
    load_prophet(city)


# Config
st.set_page_config(page_title='Monthly Predictions Hackathon',
                   page_icon=':bar_chart:', layout='wide')

st.title("MONTHLY PREDICTIONS")
st.text(" ")
# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Data Sources

# Filter
main_c1, main_c2 = st.columns(2, gap="medium")

with main_c1:
    col1, col2 = st.columns(2, gap="large")
    city_list = ['Adilabad', 'Warangal', 'Karimnagar', 'Khammam', 'Nizamabad']
    with col1:
        city = st.selectbox(
            "Select City",
            city_list
        )

    with col2:
        options = st.selectbox(
            "Select the Feature To Be Predicted",
            ("AQI", "Heatwave")
        )
if options == 'AQI':
    display_aqi(city, main_c2)
else:
    display_heatwave(city, main_c2)

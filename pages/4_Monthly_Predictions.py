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
import utils


def print_top3(df):
    col_list = list(st.columns(3, gap="medium"))
    for i in range(len(col_list)):
        with col_list[i]:
            print(df['Predictions'].iloc[i])
            st.metric(pd.to_datetime(df['Date'].iloc[i]).strftime(
                '%B'), df['Predictions'].iloc[i])


def get_statistics(df, feature):
    sorted_desc = df.sort_values('Predictions', ascending=False)
    st.title("Top 3 Months with highest {}".format(feature))
    print_top3(sorted_desc)
    sorted_asc = df.sort_values('Predictions', ascending=True)
    st.title("Top 3 Months with lowest {}".format(feature))
    print_top3(sorted_asc)


def display_aqi(city):
    st.markdown("<hr>",
                unsafe_allow_html=True)
    st.header(city)
    aqi_city = pd.read_csv(
        's3://capegemini-hackathon/predictions/aqi/{}/aqi.csv'.format(city), header=0)
    aqi_city = aqi_city[aqi_city['Date'] < '2024-01-01']
    st.markdown("<hr>",
                unsafe_allow_html=True)
    st.text("")
    st.select_slider('Pick a size', ['S', 'M', 'L'])
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.table(aqi_city)
    with col2:
        st.subheader('{} Monthly Predictions'.format(city))
        fig = utils.linegraph(aqi_city['Date'],
                              aqi_city['Predictions'], 'AQI', 'Date', 'AQI')
        st.plotly_chart(fig, use_container_width=True)
    get_statistics(aqi_city, 'AQI')


def display_heatwave(city):
    aqi_city = pd.read_csv(
        's3://capegemini-hackathon/predictions/weather/{}/weather.csv'.format(city), header=0)
    st.text("")
    st.markdown("<hr>",
                unsafe_allow_html=True)
    st.text("")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.table(aqi_city)
    with col2:
        st.subheader('{} Monthly Predictions'.format(city))
        fig = utils.linegraph(aqi_city['Date'],
                              aqi_city['Predictions'], 'Weather', 'Date', 'We')
        st.plotly_chart(fig, use_container_width=True)


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
col1, col2, col3, col4 = st.columns(4, gap="large")
with col1:
    city_list = ['Adilabad', 'Warangal', 'Karimnagar', 'Khammam', 'Nizamabad']
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
    display_aqi(city)
else:
    display_heatwave(city)

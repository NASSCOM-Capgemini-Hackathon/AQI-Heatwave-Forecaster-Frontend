# Libraries
import streamlit as st
import pandas as pd
import s3fs
import utils
from plotly_calplot import calplot
from data import get_data
from statsmodels.tsa.seasonal import seasonal_decompose
import warnings
warnings.filterwarnings("ignore")


def display_aqi(city, slider_col):

    st.header(city)
    aqi_city = get_data("dashboard-aqi", city)

    aqi_col_attributes = ['AQI', 'PM2.5', 'PM10', 'SO2', 'NO2']
    col1, col2 = st.columns(2, gap="large")

    with col1:
        aqi_attributes = st.selectbox(
            "Select Attribute",
            aqi_col_attributes
        )

    with col2:
        start_month, end_month = st.select_slider('Pick Month Range', options=(aqi_city['DATE']), value=(
            aqi_city['DATE'].iloc[0], aqi_city['DATE'].iloc[-1]))

    aqi_city = aqi_city[(aqi_city['DATE'] >=
                        start_month) & (aqi_city['DATE'] <= end_month)]

    fig = utils.linechart_with_range_slider(aqi_city['DATE'],
                                            aqi_city[aqi_attributes], aqi_attributes, 'Time Series data with Rangeslider for {} in {}'.format(aqi_attributes, city))
    st.plotly_chart(fig, use_container_width=True)

    heatmap_fig = utils.heat_map_chart(
        aqi_city[aqi_col_attributes], "Correlation between Features")
    st.plotly_chart(heatmap_fig, use_container_width=True)

    fig = calplot(aqi_city,showscale=True, name=aqi_attributes, month_lines_width=15,
                  month_lines_color='#FFFFFF', title="Calender Heatmap for attribute {} in {}".format(aqi_attributes,city) ,x='DATE', y=aqi_attributes)
    st.plotly_chart(fig, use_container_width=True)

    analysis = aqi_city[[aqi_attributes]].copy()
    decompose_result_mult = seasonal_decompose(
        analysis, model="additive", period=int(len(aqi_city)/2), extrapolate_trend='freq')
    statmodel_fig = utils.plot_seasonal_decompose(
        decompose_result_mult, city, aqi_attributes, dates=aqi_city['DATE'])
    st.plotly_chart(statmodel_fig, use_container_width=True)


def display_heatwave(city, slider_col):
    st.header(city)
    weather_city, weather_attributes = get_data("dashboard-weather", city)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        weather_attributes = st.selectbox(
            "Select Attribute",
            weather_attributes
        )

    with col2:
        start_month, end_month = st.select_slider('Pick Month Range', options=(weather_city['DATE']), value=(
            weather_city['DATE'].iloc[0], weather_city['DATE'].iloc[-1]))

    weather_city = weather_city[(weather_city['DATE'] >=
                                 start_month) & (weather_city['DATE'] <= end_month)]

    fig = utils.linechart_with_range_slider(weather_city['DATE'],
                                            weather_city[weather_attributes], weather_attributes, 'Time Series data with Rangeslider for {} in {}'.format(weather_attributes, city))
    st.plotly_chart(fig, use_container_width=True)

    heatmap_fig = utils.heat_map_chart(
        weather_city, "Correlation between Features")
    st.plotly_chart(heatmap_fig, use_container_width=True)

    fig = calplot(weather_city,showscale=True,title="Calender Heatmap for attribute {} in {}".format(weather_attributes,city),name=weather_attributes, month_lines_width=15,
                  month_lines_color='#FFFFFF', x='DATE', y=weather_attributes)
    st.plotly_chart(fig, use_container_width=True)

    analysis = weather_city[['Max Temp']].copy()
    decompose_result_mult = seasonal_decompose(
        analysis, model="multiplicative", period=int(len(weather_city)/2), extrapolate_trend='freq')
    statmodel_fig = utils.plot_seasonal_decompose(
        decompose_result_mult, city, 'Max Temp', dates=weather_city['DATE'])
    st.plotly_chart(statmodel_fig, use_container_width=True)


# Config
st.set_page_config(page_title='Dashboard AQI & Heatwave',
                   page_icon=':bar_chart:', layout='wide')

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
            "Select the Feature To Be Viewed",
            ("Heatwave", "AQI")
        )

if options == 'AQI':
    display_aqi(city, main_c2)
elif options == "Heatwave":
    display_heatwave(city, main_c2)

# Libraries
import streamlit as st
from data import get_data

# Confit
st.set_page_config(page_title='AQI Weather Forecaster',
                   page_icon=':bar_chart:', layout='wide', initial_sidebar_state='collapsed')

city = st.selectbox("SELECT ANY ONE OF THE CITY ", ("Adilabad",
                    "Nizamabad", "Khammam", "Warangal", "Karimnagar"))

temp_unit = " °C"
wind_unit = " km/h"

df, bar_fig, line_fig, temp, current_weather, icon = get_data("Get current data",city)

col1, col2 = st.columns(2)
with col1:
    st.write("## Current Temperature ")
with col2:
    st.image(
        f"http://openweathermap.org/img/wn/{icon}@2x.png")

col1, col2 = st.columns(2)
col1.metric("TEMPERATURE", temp+temp_unit)
col2.metric("WEATHER", current_weather)

tab1, tab2 = st.tabs(["Bar Graph", "Line Graph"])

with tab1:
    st.plotly_chart(bar_fig, use_container_width=True)

with tab2:
    st.plotly_chart(line_fig, use_container_width=True)

st.table(df)

col1, col2, col3 ,col4 ,col5 ,col6 ,col7 = st.columns(7)
with col1:
   st.header("A dog")

with col2:
   st.header("A dog")

with col3:
   st.header("An owl")

with col4:
   st.header("A cat")

with col5:
   st.header("A dog")

with col6:
   st.header("An owl")

with col7:
   st.header("asds")
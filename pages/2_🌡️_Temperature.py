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
theme_plotly = "streamlit" # None or streamlit

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
    history_url="https://aqi-heatwave-app.azurewebsites.net/api/weather/getHistoryDailyWeather"
    future_url = "https://aqi-heatwave-app.azurewebsites.net/api/weather/getDailyWeatherPredictions"

    # Define the request payload
    payload = {
        "City":city
    }

    # Send the POST request and store the response in a variable
    r1 = requests.post(history_url, json=payload)
    data1=json.loads(r1.text)
    # Convert the response to a pandas DataFrame
    df_hist=json_normalize(data1)
    

    

    # Convert the datetime string to a datetime object
    df_hist['DATE'] = pd.to_datetime(df_hist['DATE'])

    # Format the datetime object as "YYYY-MM-DD" and store it in a new column
    df_hist['DATE'] = df_hist['DATE'].dt.strftime('%Y-%m-%d')

    # Drop the original datetime string and datetime columns
  
     # Display the resulting DataFrame

    df_hist['Max Temp']=np.round(df_hist['Max Temp'])

    r2 = requests.post(future_url, json=payload)
    data2=json.loads(r2.text)
    
    df_fut=json_normalize(data2)
    df_fut['Predictions']=np.round(df_fut['Predictions'])

    with st.container():
        
        st.markdown("<h2 style='font-family:Verdana'><b>CURRENT TEMPERATURE</b></h2>", unsafe_allow_html=True)
        st.markdown("""---""")
        
        
        today_date=str(date.today())
    
   
        today_aqi= df_hist.loc[df_hist['DATE'] == today_date, 'Max Temp'].values[0]
        
       
        fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = today_aqi,
        mode = "gauge+number",
        title = {'text': "TEMPERATURE"},
        
        gauge = {'axis': {'range': [None, 500]},
                'steps' : [
                    {'range': [0, 250], 'color': "lightgray"},
                    {'range': [250, 400], 'color': "gray"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
        
        st.plotly_chart(fig,use_container_width=True)
            
        #text=get_aqi_message(today_aqi)
        #st.markdown(f"<h3 style='font-family:Verdana'>{text}</h3>", unsafe_allow_html=True)

        
    
    st.write('')
    st.write('')
    with st.container():
        
        st.markdown("<h2 style='font-family:Verdana'><b>DAILY TEMPERATURE FORECAST</b></h2>", unsafe_allow_html=True)
        st.markdown("""---""")
        
        fig = go.Figure(data=go.Bar(x=df_fut['Date'], y=df_fut['Predictions']))


        fig.update_layout(     
            xaxis_title='Date',
            yaxis_title='Temperature'
        )
        st.plotly_chart(fig,use_container_width=True)

       


def display_monthly(city):
    history_url=""
    future_url = "https://aqi-heatwave-app.azurewebsites.net/api/aqi/getMonthlyAQIPredictions"

    payload = {
        "City":city
    }

   
    r1 = requests.post(history_url, json=payload)
    data1=json.loads(r1.text)
  
    df_hist=json_normalize(data1)
    df_hist['DATE'] = pd.to_datetime(df_hist['DATE'])

    
    df_hist['DATE'] = df_hist['DATE'].dt.strftime('%Y-%m-%d')
    df_hist['Max Temp']=np.round(df_hist['Max Temp'])
   
    r2 = requests.post(future_url, json=payload)
    data2=json.loads(r2.text)
 
    df_fut=json_normalize(data2)
    df_fut['Predictions']=np.round(df_fut['Predictions'])
    

    with st.container():
        st.markdown("<h2 style='font-family:Verdana'><b>CURRENT TEMPERATURE</b></h2>", unsafe_allow_html=True)
        st.markdown("""---""")
      
        today_date=date.today()
        res = today_date.replace(day=1)
        
        today_aqi= df_hist.loc[df_hist['DATE'] == str(res), 'Max Temp'].values[0]

        fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = today_aqi,
        mode = "gauge+number",
        title = {'text': "TEMPERATURE"},
        
        gauge = {'axis': {'range': [None, 500]},
                'steps' : [
                    {'range': [0, 250], 'color': "lightgray"},
                    {'range': [250, 400], 'color': "gray"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
        
        st.plotly_chart(fig,use_container_width=True)
       


        
        #text=get_aqi_message(today_aqi)
        #st.markdown(f"<h3 style='font-family:Verdana'>{text}</h3>", unsafe_allow_html=True)

        #st.write(hasClicked)
    
    st.write('')
    st.write('')
    with st.container():
        st.markdown("<h2 style='font-family:Verdana'><b>MONTHLY TEMPERATURE FORECAST</b></h2>", unsafe_allow_html=True)
        st.markdown("""---""")
        
        
        fig = go.Figure(data=go.Bar(x=df_fut['Date'], y=df_fut['Predictions']))


        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Temperature'
        )
        st.plotly_chart(fig,use_container_width=True)



st.set_page_config(page_title='Temperature', page_icon=':bar_chart:', layout='wide')
st.text("")
st.text("")

st.markdown("<h1 style='text-align: center; color: #D81F26; font-family:Verdana'><b>🌡️ TEMPERATURE</b></h1>", unsafe_allow_html=True)
st.text(" ")
st.text(" ")

with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

options = st.sidebar.selectbox(
    "Select the Frequency for Temperature",
    ("Daily","Monthly")
)
city_list=['Adilabad','Warangal','Karimnagar','Khammam','Nizamabad']
city = st.sidebar.selectbox(
    "Select City",
    city_list
)

if options=='Daily':
    display_daily(city)
else:
    display_monthly(city)
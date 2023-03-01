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
from datetime import datetime
from scipy.stats import skew


theme_plotly = "streamlit"

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

def calc_skew(df,target):
    
    skewness = skew(df[target])

    # determine skewness type based on skewness coefficient
    if skewness > 0:
        return "The AQI data is right-skewed"
    elif skewness < 0:
        return "The AQI data is left-skewed"
    else:
        return "The AQI data is normally distributed"

def get_statistics(df,target):
    median=np.mean(df[target].values)
    max=np.max(df[target].values)
    min=np.min(df[target].values)
    return min,median,max
    
def print_3(stat,names):
    col_list = list(st.columns(3, gap="medium"))
    for i in range(len(col_list)):
        with col_list[i]:
            # print(df['Predictions'].iloc[i])
            st.metric(names[i],int(np.round(stat[i])))

def display_daily(city):
    


    history_url="https://aqi-heatwave-app.azurewebsites.net/api/aqi/getHistoryDailyAQI"
    future_url = "https://aqi-heatwave-app.azurewebsites.net/api/aqi/getDailyAQIPredictions"

   
    payload = {
        "City":city
    }

    r1 = requests.post(history_url, json=payload)
    data1=json.loads(r1.text)
   
    df_hist=json_normalize(data1)
    df_hist['DATE'] = pd.to_datetime(df_hist['DATE'])
    df_hist['DATE'] = df_hist['DATE'].dt.strftime('%Y-%m-%d')
    df_hist['AQI']=np.round(df_hist['AQI'])
    r2 = requests.post(future_url, json=payload)
    data2=json.loads(r2.text)
    
    
    df_fut=json_normalize(data2)
    df_fut['Predictions']=np.round(df_fut['Predictions'])
    df_fut.rename(columns={'Date':'DATE'},inplace=True)
    
    df_res=pd.merge(df_hist,df_fut,on='DATE',how='outer')

    with st.container():
        
        st.subheader("Daily Air Quality Index Predictions")
        st.markdown("""---""")

        data = go.Scatter(
            x = df_res["DATE"],
            y = df_res["AQI"],
            mode = 'lines',
            name="Data values"
        )

        pred = go.Scatter(
            x = df_res["DATE"],
            y = df_res["Predictions"],
            mode = 'lines',
             
            line = {"color": "#9467bd"}, 
            name="Forecast"
        )

    
        data = [data,pred]

        layout = go.Layout(title="AQI Forecast")

        fig = go.Figure(data=data,layout=layout)
        st.plotly_chart(fig,use_container_width=True)

        st.text(' ')
        st.text(' ')
        st.markdown('---')
        
    with st.container():
        st.subheader("Daily AQI Data Statistics")
        
        st.markdown('---')
        res=get_statistics(df_hist,'AQI')
        stat=['Minimum','Median','Maximum']
        print_3(res,stat)
        fig = px.histogram(df_hist, x="AQI",title='AQI Distribution',marginal='box')
        st.plotly_chart(fig,use_container_width=True)
        min_date=df_hist.loc[df_hist['AQI']==res[0],'DATE'].iloc[0]
        max_date=df_hist.loc[df_hist['AQI']==res[2],'DATE'].iloc[0]
        st.markdown(
                    f"""
                    **Inference:**
                    - **Minimum AQI for {city} was on {min_date}**
                    - **Maximum AQI for {city} was on {max_date}**
                    - **{calc_skew(df_hist,'AQI')}**
                    """
                    )

        
        
        

       


def display_monthly(city):
    history_url="https://aqi-heatwave-app.azurewebsites.net/api/aqi/getHistoryMonthlyAQI"
    future_url = "https://aqi-heatwave-app.azurewebsites.net/api/aqi/getMonthlyAQIPredictions"

    payload = {
        "City":city
    }

   
    r1 = requests.post(history_url, json=payload)
    data1=json.loads(r1.text)
  
    df_hist=json_normalize(data1)
    df_hist['DATE'] = pd.to_datetime(df_hist['DATE'])

    
    df_hist['DATE'] = df_hist['DATE'].dt.strftime('%Y-%m-%d')
    df_hist['AQI']=np.round(df_hist['AQI'])
    
    r2 = requests.post(future_url, json=payload)
    data2=json.loads(r2.text)
 
    df_fut=json_normalize(data2)
    df_fut['Predictions']=np.round(df_fut['Predictions'])
    df_fut.rename(columns={'Date':'DATE'},inplace=True)
    
    df_res=pd.merge(df_hist,df_fut,on='DATE',how='outer')
    
    with st.container():
        st.text(' ')
        st.text(' ')
        st.markdown('---')
        st.subheader("Monthly Air Quality Index Predictions")
        st.markdown("""---""")

        data = go.Scatter(
            x = df_res["DATE"],
            y = df_res["AQI"],
            mode = 'lines',
            name="Data values"
        )

        pred = go.Scatter(
            x = df_res["DATE"],
            y = df_res["Predictions"],
            mode = 'lines',
             
            line = {"color": "#9467bd"}, 
            name="Forecast"
        )

    
        data = [data,pred]

        layout = go.Layout(title="AQI Forecast")

        fig = go.Figure(data=data,layout=layout)
        st.plotly_chart(fig,use_container_width=True)

        st.text(' ')
        st.text(' ')
        st.markdown('---')
    
    with st.container():
        
        st.subheader("Monthly AQI Data Statistics")
        st.markdown('---')
        res=get_statistics(df_hist,'AQI')
        stat=['Minimum','Median','Maximum']
        print_3(res,stat)
        fig = px.histogram(df_hist, x="AQI",title='AQI Distribution',marginal='box')
        st.plotly_chart(fig,use_container_width=True)
        min_date=df_hist.loc[df_hist['AQI']==res[0],'DATE'].iloc[0]
        max_date=df_hist.loc[df_hist['AQI']==res[2],'DATE'].iloc[0]
        st.markdown(
                    f"""
                    **Inference:**
                    - **Minimum AQI for {city} was on {datetime.strptime(min_date,'%Y-%m-%d').strftime('%B %Y')}**
                    - **Maximum AQI for {city} was on {datetime.strptime(max_date,'%Y-%m-%d').strftime('%B %Y')}**
                    - **{calc_skew(df_hist,'AQI')}**
                    """
                    )
    
    

        


st.set_page_config(page_title='Air Quality Index', page_icon=':bar_chart:', layout='wide')
st.text("")
st.text("")

st.title("🏭 AIR QUALITY INDEX")
st.text(" ")
st.text(" ")

with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


city_list=['Adilabad','Warangal','Karimnagar','Khammam','Nizamabad']
city = st.selectbox(
    "Select City",
    city_list
)
st.markdown('---')


display_daily(city)
display_monthly(city)
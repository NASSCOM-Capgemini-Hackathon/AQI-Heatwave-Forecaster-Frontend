from plotly import graph_objects as go
import requests
import json
from pandas import json_normalize
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


URL_MAPPING = {'Adilabad': 'https://www.aqi.in/dashboard/india/telangana/adilabad',
               'Nizamabad': 'https://www.aqi.in/dashboard/india/telangana/nizamabad',
               'Khammam': 'https://www.aqi.in/dashboard/india/telangana/khammam',
               'Warangal': 'https://www.aqi.in/dashboard/india/telangana/warangal',
               'Karimnagar': 'https://www.aqi.in/dashboard/india/telangana/karimnagar'
               }
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}


def get_current_aqi(city):
    global URL_MAPPING, HEADERS
    req = Request(URL_MAPPING[city], headers=HEADERS)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "html.parser")
    aqi_val = soup.find('table', {"id": "state-table"})
    table_col, table_data = aqi_val.find('thead'),  aqi_val.find('tbody')
    table_data = table_data.find_all('td')
    table_col = table_col.find_all('th')[1:]
    for val in zip(table_col, table_data):
        name, value = val
        name, value = name.get_text().strip(), value.get_text().strip()
        value = value.replace(",", '')
        if name == 'AQI-IN':
            return (value)


def get_request_data(url, cityname):
    payload = {
        "City": cityname
    }

    r1 = requests.post(url, json=payload)
    data1 = json.loads(r1.text)
    df_fut = json_normalize(data1)
    return df_fut


def bargraph(x_data, y_data1, y_data1_name, xaxis_title, yaxis_title, y_data2=None, y_data2_name=None):
    """
    """
    if y_data2 == None and y_data2_name == None:
        fig = go.Figure(data=[
            go.Bar(name=y_data1_name, x=x_data,
                   y=y_data1, marker_color='crimson'),
        ])
    else:
        fig = go.Figure(data=[
            go.Bar(name=y_data1_name, x=x_data,
                   y=y_data1, marker_color='crimson'),
            go.Bar(name=y_data2_name, x=x_data, y=y_data2, marker_color='navy')
        ])

    fig.update_layout(xaxis_title=xaxis_title,
                      yaxis_title=yaxis_title, barmode='group')
    return fig


def linegraph(x_data, y_data1, y_data1_name, xaxis_title, yaxis_title, y_data2=None, y_data2_name=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data1, name=y_data1_name))
    if y_data2_name != None:
        fig.add_trace(go.Scatter(x=x_data, y=y_data2,
                                 name=y_data2_name, marker_color='crimson'))
    fig.update_layout(
        xaxis_title=xaxis_title, yaxis_title=yaxis_title, font=dict(color="white"))
    return fig

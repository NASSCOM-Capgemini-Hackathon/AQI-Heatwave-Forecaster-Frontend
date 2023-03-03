## AQI-Heatwave-Forecaster-Frontend

Frotend Application  bulit for NASSCOM Hackathon 2023 using streamlit  which aims in providing interactive application for the task of predicting AQI and Heat wave occurences in Tier-2 cities of Telenagana


## Preview of Application

![Screenshot 2023-03-03 190129](https://user-images.githubusercontent.com/62760269/222732893-fe997643-bca6-4781-b1fd-80a686ff8f63.png)

## Website Link

https://nasscom-capgemini-hackathon-aqi-heatwave-forecaster-home-o0tty0.streamlit.app/Live_Dashboard

## Setting Up Application

1. Create and Activate the virtual env
```
    python3 -m venv venv
    venv\Scripts\activate.bat
```

2. Install the required python packages
```
    pip3 install -r requirements.txt
```

3. Run the Streamlit Application
```
    streamlit run home.py
```


## Page Structure

1. Home Page

   
   ![chrome-capture-2023-2-3 (1)](https://user-images.githubusercontent.com/62760269/222749637-67691f0a-aba5-43fc-b55a-67dc3696d324.gif)


   Displays the monthly wise forecast for AQI and Heat wave occurence for the year of 2023 with necessary visualizations.The Best time series model for forecasting the results was based on RMSE and the description about the model chosen is provided. The evaluation metric displayed on the page is based on 25% of the data.
   

2. AQI

   ![chrome-capture-2023-2-3 (2)](https://user-images.githubusercontent.com/62760269/222746495-69447994-632e-4cfc-b2a1-3d5fb5de79f6.gif)


   Displays the Dynamic AQI Predictions monthly/Daily wise which is fetched from our back end API based on the model produced values returned by AWS scheduler. The page gets dynamically updated every day once the scheduler gets running. Forecasted values for the next 15 days/15 months is shown on the page with visualizations.
  

3. Temperature

   ![chrome-capture-2023-2-3 (3)](https://user-images.githubusercontent.com/62760269/222746900-6ef561b8-8d84-43d2-8577-69e34391542f.gif)


   Displays the Dynamic Temperature Predictions monthly/Daily wise which is fetched from our back end API based on the model produced values returned by AWS scheduler. The page gets dynamically updated every day once the scheduler gets running. Forecasted values for the next 15 days/15 months is shown on the page with visualizations.
  

4. Live Dashboard

   ![chrome-capture-2023-2-3 (4)](https://user-images.githubusercontent.com/62760269/222747494-f995d63a-6cdd-4e02-9b89-5ee643c3f6f4.gif)


   Diplays the AQI data fetched from https://www.aqi.in/in/dashboard/india/telangana and the temperature data fetched from https://api.openweathermap.org/data/2.5/weather. The current data as well as the forecast results for the upcoming week is displayed with charts for the given city.

5. EDA

   ![chrome-capture-2023-2-3 (9)](https://user-images.githubusercontent.com/62760269/222749149-a23bc99e-8e50-43d7-add7-289779abf933.gif)

   
   The charts that support our assumptions and which has guided in model training for AQI and Heatwave data for the given city are displayed. A brief work flow regarding the modelling process of given data is also provided.
  
6. About Us

   Displays the breief details oyr group along with our startup plan!
  
  
 


# Libraries
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from streamlit_card import card
from datetime import date
import warnings
warnings.filterwarnings("ignore")

st.header("ABOUT US")
st.markdown("<hr>", unsafe_allow_html=True)
st.header("START UP PLAN")
st.markdown("<hr>", unsafe_allow_html=True)
st.header("TEAM PSG DS 2K19")
st.markdown("<hr>", unsafe_allow_html=True)
user1_col1, padding, user1_col2 = st.columns((6, 1, 15), gap="small")
with user1_col1:
    ashish = Image.open('./images/Ashish.jpg')
    ashish = ashish.resize((400, 500))
    st.image(ashish, caption="Team Member 1 - Ashish")
with user1_col2:
    st.header("Ashish K")
    st.write("""Hello This is Ashish K, from PSG College of Technology currently pursuing my 4th year MSc Data Science course at PSG College of Technology.\n
    AREAS OF INTEREST : MACHINE LEARNING\n
    WORK EXPERIENCE   : Summer Intern At Goldman Sachs\n
    GITHUB PROFILE    : https://github.com/Ashishkumaraswamy\n
    LINKEDIN URL      : https://www.linkedin.com/in/ashish-kumaraswamy/\n
    ROLE IN HACKATHON : Developed the scheduler scripts running in AWS\n
                        so as to get dynamic predictions taking into account\n
                        of the current values. Developed the hourly, daily and\n
                        monthly schedulers for this work and storing the results\n 
                        in AWS S3 bucket.   
    """)
st.markdown("<hr>", unsafe_allow_html=True)
user2_col1, padding, user2_col2 = st.columns((15, 1, 6), gap="small")
with user2_col2:
    jega = Image.open('./images/mathan.jpg')
    jega = jega.resize((400, 500))
    st.image(jega, caption="Team Member 2 - Mathana Maathav")
with user2_col1:
    st.header("Mathana Maathav")
    st.write("""Hello This is Mathana Maathav, from PSG College of Technology currently pursuing my 4th year MSc Data Science course at PSG College of Technology.\n
    AREAS OF INTEREST : MACHINE LEARNING\n
    WORK EXPERIENCE   : SDE Summer Intern At Zerodown\n
    GITHUB PROFILE    : https://github.com/mathanamathav\n
    LINKEDIN URL      : https://www.linkedin.com/in/mathana-mathav-a-s-615b65205/\n
    ROLE IN HACKATHON : Developed the scheduler scripts running in AWS\n
                        so as to get dynamic predictions taking into account\n
                        of the current values. Developed the hourly, daily and\n
                        monthly schedulers for this work and storing the results\n 
                        in AWS S3 bucket.   
    """)
st.markdown("<hr>", unsafe_allow_html=True)
user3_col1, padding, user3_col2 = st.columns((6, 1, 15), gap="small")
with user3_col1:
    jega = Image.open('./images/jega.png')
    jega = jega.resize((400, 500))
    st.image(jega, caption="Team Member 3 - Jegadeesh M S")
with user3_col2:
    st.header("Jegadeesh M S")
    st.write("""Hello This is Jegadeesh M S, from PSG College of Technology currently pursuing my 4th year MSc Data Science course at PSG College of Technology.\n
    AREAS OF INTEREST : MACHINE LEARNING\n
    WORK EXPERIENCE   : Data Analyst Summer Intern At Buckman\n
    GITHUB PROFILE    : https://github.com/jegadeesh2001\n
    LINKEDIN URL      : https://www.linkedin.com/in/jegadeesh-manickam-9b112597/\n
    ROLE IN HACKATHON : Worked on Timeseries forecasting of AQI and\n
                        Heatwave occurence for different cities along with the\n
                        corresponding model evaluation. The results were then\n
                        deployed to our streamlit application. 
    """)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:52:59 2022

@author: namnguyen
"""



#import numpy as np
#import math
import streamlit as st
#from math import pi, cos, sin
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from matplotlib.animation import PillowWriter
import pandas as pd
import os
#import base64
#from PIL import Image
#import io
path= os.getcwd()


#%%
st.title('General introduction')
st.image("https://media-exp1.licdn.com/dms/image/C4E0BAQF-5O5stYOVnA/company-logo_200_200/0/1519880154681?e=2147483647&v=beta&t=JfMPNm2p8aQC7iHLqp8S4096lFDmShsodp8A73sRnWQ",width=100)
st.header('Company: CFC.SL' )
st.markdown("**Pedram Manouchehri** ")
st.markdown("**Nam Nguyen** ")
  
st.write('**************************************')

st.subheader("Introduction:")
#st.markdown('Streamlit is **_really_ cool**.')

st.markdown("**Plotly Dash vs Streamlit — Which is the best?**")
st.markdown("[History of GitHub stars for both Plotly Dash and Streamlit](https://towardsdatascience.com/plotly-dash-vs-streamlit-which-is-the-best-library-for-building-data-dashboard-web-apps-97d7c98b938c)")
image = "https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png"

st.image(image, caption='The fastest way to build and share data apps')
st.write('Streamlit is an open source app framework in Python. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy, NumPy, pandas, Matplotlib etc.')

st.write('**************************************')
st.subheader("Apply data science in structural engineering")
st.markdown("[Projectile Motion](https://namnguyen2015-projectile-mot-220901-streamlit-projectile-8zn9wi.streamlitapp.com/)")
st.markdown("[Data Analysis](https://namnguyen2015-data-analysis-streamlit-data-analysis-ws79u1.streamlitapp.com/)")



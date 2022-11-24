# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:07:56 2022

@author: kohm
"""

import yfinance as yf
import streamlit as st
import pandas as pd
pd.set_option('display.max_columns', None)

# Following markdown
st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!
         
         """)
         
tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-05-31',end='2020-05-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


from tracemalloc import start
from pyparsing import GoToColumn
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
""")
name = ""
col1, col2, col3 = st.columns(3)
tickerSymbol = ""

with col1:
    googleBtn = st.button("Google Stock")
with col2:
    appleBtn = st.button("Apple Stock")
with col3:
    telsaBtn = st.button("Tesla Stock")

if googleBtn:
    tickerSymbol = "GOOGL"
    name = "Google"
elif appleBtn:
    tickerSymbol = "AAPL"
    name = "Apple"
elif telsaBtn:
    tickerSymbol = "TSLA"
    name = "Tesla"

st.write(f"Shown are the stock of {name}")
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(
    period="1d", start="2010-5-31", end="2020-5-31")
st.write(""" 
**Closing Price:**
 """)
st.line_chart(tickerDf.Close)
st.write(""" 
**Volume:**
 """)
st.line_chart(tickerDf.Volume)

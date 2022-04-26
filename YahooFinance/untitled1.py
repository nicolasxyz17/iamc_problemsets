# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:52:16 2022

@author: NicolasToledo
"""
import yfinance as yf
data = yf.download("AAPL", start="2020-01-01", end_date="2021-01-01")['Adj Close']
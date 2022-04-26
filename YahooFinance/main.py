"""
Created on Sun Apr 24 16:37:39 2022

@author: NicolasToledo
"""

import pandas as pd
import yfinance as yf

class YahooAdjPrice:
    @staticmethod
    def getAdjPrice(ticker: str, start_date: str, end_date: str) -> pd.DataFrame():
        pxData = pd.DataFrame()
        for t in ticker:
            data = yf.download(t, start=start_date, end_date=end_date)
            data.rename(columns={"Adj Close":t}, inplace=True)
            data.drop (["Open","High","Low","Close","Volume"], axis=1, inplace=True)
            pxData = pxData.merge(data, right_index=True, left_index=True, how="outer")
        return pxData

tickers = ["TSLA","TWTR"]
pxData = YahooAdjPrice.getAdjPrice(tickers,start_date='2022-01-01',end_date='2022-04-22')
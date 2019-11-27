import pandas as pd
import numpy as np
import json
import yfinance as yf
import nltk

def get_tweet_data():
    #download and save tweet data
    
    with open('tweets-to-Nov.json', 'rb') as f: 
        data = json.load(f) 
    
    df = pd.DataFrame(data)
    df.to_excel('tweets-to-Nov.xls', index=False)
    return df

def get_financial_data():
    #download and save financial data
    
    df = yf.download("^GSPC", start="2018-01-01", end="2019-11-25", interval='60m')
    df['date'] = df['date'].astype(str)
    df.to_excel('S&P 500_hour.xls')
    return df

def get_data():
    #read all the necessary data
    
    df1 = pd.read_excel('tweets.xls')
    df2 = pd.read_excel('S&P 500.xls')
    return df1, df2

def get_labels(df):
    #Convert stock market prices to ups(1) and downs(0) based on the close prices
    
    return (df2['Close'].shift(-1) > df2['Close']) * 1
    

#df1, df2 = get_data()
#y = get_labels(df2)
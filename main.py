import pandas as pd
import numpy as np
import json
import yfinance as yf
import nltk

def get_tweet_data():
    #download and save tweet data
    
    with open('tweets.json', 'rb') as f: 
        data = json.load(f) 
    
    df = pd.DataFrame(data)
    df.to_excel('tweets.xls', index=False)
    return df

def get_financial_data():
    #download and save financial data
    
    df = yf.download("^GSPC", start="2005-01-01", end="2019-10-1")
    df.to_excel('S&P 500.xls')
    return df

def get_data():
    #read all the necessary data
    
    df1 = pd.read_excel('tweets.xls')
    df2 = pd.read_excel('S&P 500.xls')
    return df1, df2

df1, df2 = get_data()
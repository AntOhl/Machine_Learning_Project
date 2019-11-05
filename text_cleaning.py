# Import libraries


import pandas as pd
import numpy as np
import json
import yfinance as yf
import nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer



def get_tweet_data():
    # Download and save tweet data

    with open('tweets.json', 'rb') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df.to_excel('tweets.xls', index=False)
    return df


df1 = get_tweet_data()

df1

df1['text']


# Add word_count column

df1['word_count'] = df1['text'].apply(lambda x: len(str(x).split(" ")))

df1[['text', 'word_count']]


# Word count statistical description

df1[['text', 'word_count']].describe()


# 1-word tweets, usually hhtp links, # tags or @ tags)

df1[['text', 'word_count']][df1['word_count'] == 1].head()
df1[['text', 'word_count']][df1['word_count'] == 1].count()


# 20 most common words

freq_common = pd.Series(' '.join(df1['text']).split()).value_counts()[:20]
freq_common


# 20 less common words

freq_uncommon = pd.Series(' '.join(df1['text']).split()).value_counts()[-20:]
freq_uncommon


# Remove 'RT + source account' from tweets

retweets = df1["text"][df1['is_retweet'] == True]
removeRT = retweets.str[3:]
cleanretweets = removeRT.str.split(n=1).str[1]
df1["text"][df1['is_retweet'] == True] = cleanretweets
df1["text"][df1['is_retweet'] == True]


# Setting frequent words without contextual meaning, 'stop_words' is built-in, 'new_words' is chosen.

stop_words = set(stopwords.words('english'))
new_words = ["using", "show", "result", "large", "also", "iv", "one", "two", "new", "previously", "shown"]
stop_words = stop_words.union(new_words)


# Removing links from tweets

#the old code
#df1["cleantext1"] = df1['text'].str.replace(
#    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "")

r = '(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
df1["cleantext1"] = df1['text'].str.replace(r, '')
df1["cleantext1"]


# Remove punctuation

df1["cleantext2"] = df1["cleantext1"].str.replace('[^\w\s]', '')
df1["cleantext2"]


# Remove special characters and digits

df1["cleantext3"] = df1["cleantext2"].str.replace("(\\d|\\W)+", " ")
df1["cleantext3"]


# Put all words in lower case

df1["cleantext4"] = df1["cleantext3"].str.lower()
df1["cleantext4"]

# 20 most common words after cleaning

freq_common = pd.Series(' '.join(df1['cleantext4']).split()).value_counts()[:20]
freq_common


# 20 less common words after cleaning

freq_uncommon = pd.Series(' '.join(df1['cleantext4']).split()).value_counts()[-20:]
freq_uncommon

'''
Ruixu:
1. Do we need to remove tags all together? @realDonaldTrump for example? 
If we dont do so we will end up with someting as weird as m_forese. 
2. We failed to remove links such as www.youtube.com/user/mattressserta (fixed)
3. We failed to remove punctuations such as '_' probably from hashtags like 'suffolk_sheriff'.
Do we need to replace '_' with a space then?
4. What does 'Remove 'RT + source account' from tweets' mean?
'''

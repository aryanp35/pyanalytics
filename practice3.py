# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:17:10 2019

@author: Aryan
"""

#Topic: Stock - SBI
#-----------------------------
#libraries

#Indian Equities
#https://www.quandl.com/data/TC1-Indian-Equities-Adjusted-End-of-Day-Prices
#quandl.get("TC1/SBIN", start_date="1970-01-01", end_date="1970-01-01")
#pip install quandl #install as admin in anaconda
#register in quandl and create your own keys
#https://www.quandl.com/data/TC1/SBIN-State-Bank-of-India-Adjusted-Pricing
import quandl
import pandas as pd
import datetime

start1 = datetime.datetime(2017, 1, 1)
end1 = datetime.datetime(2019, 7, 20)
key = 'osYk6zbrPAmBcx_ngjaq'
S_sbi = "BSE/BOM500112" # SBI
#Fetch Data
sbi= quandl.get(dataset=S_sbi, authtoken=key, start_date=start1, end_date=end1)
sbi.head()
#Analyse
sbi.Close.plot(figsize=(15,10))
plt.show();
#Plots
data=sbi.copy()
data.columns
data.dtypes
data.head()
data.index
data[['Open','High','Low','Close']]
data[['Open','High','Low','Close','WAP']].plot(figsize=(15,12))
data[['Open','Close']].plot()
#%%%
#Libraries
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
mondays = WeekdayLocator(MONDAY) # major ticks on the mondays
alldays = DayLocator() # minor ticks on the days
weekFormatter = DateFormatter('%b %d') # e.g., Jan 12
dayFormatter = DateFormatter('%d') # e.g., 12

#prepare OHLC
sbi.head()
data3 = sbi[['Open', 'High', 'Low', 'Close']].copy()
data3.head()
data3.tail()
date1 = "2019-1-1"
date2 = "2019-7-30"
data3b = data3[(data3.index >= date1) & (data3.index <= date2)]
data3b
#%%% Plots
#run together till plt.show
#https://pythonprogramming.net/candlestick-ohlc-graph-matplotlib-tutorial/
fig, ax = plt.subplots(figsize=(10,8))
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)
candlestick_ohlc( ax, zip( mdates.date2num (data3b.index.to_pydatetime()), data3b[ 'Open'], data3b['High'],data3b['Low'], data3b['Close']),width=0.6)
ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment= 'right')
plt.show();
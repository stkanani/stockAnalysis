#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


start = datetime.datetime(2018,1,1)
end = datetime.datetime(2021,12,12)


# In[25]:


# This will get the data for 3 companies
# It can be modified by changing each company name
# In this example it is reading the Tesla, Ford and GM Stock using DataREader
tesla  = web.DataReader("TSLA",'yahoo',start,end)
toyota = web.DataReader("TM",'yahoo',start,end)
gm = web.DataReader("GM",'yahoo',start,end)


# In[32]:


#Save the stock information in the CSV
tesla.to_csv('Tesla_Stock_20180101_20211212.csv')
toyota.to_csv('Toyota_Stock_20180101_20211212.csv')
gm.to_csv('GM_Stock_20180101_20211212.csv')


# In[27]:


# Read Tesla data
tesla.head()


# In[28]:


# Read Ford data
toyota.head()


# In[29]:


# Read GM data
gm.head()


# In[34]:


#Comparing the Open prices for each of the companies and create the plot
#Options are High,Low,Open,Close,Volume
tesla['Open'].plot(label='Tesla',figsize=(20,10))
toyota['Open'].plot(label='Toyota')
gm['Open'].plot(label='GM')
plt.ylabel('Stock Price')
plt.title('Stock Prices for Tesla, GM and Toyota')
plt.legend() # To put a legend for it
plt.show()


# In[33]:


#Comparing the Volume for each of the companies and create the plot
tesla['Volume'].plot(label='Tesla',figsize=(20,10))
toyota['Volume'].plot(label='Toyota')
gm['Volume'].plot(label='GM')
plt.ylabel('Volume')
plt.title('Stock Prices for Tesla, GM and Toyota')
plt.legend() # To put a legend for it
plt.show()


# In[47]:


#This will create columntal amount of money traded for each company
#To Calculate it will multiply Open price by the volume
tesla['Total Traded'] = tesla ['Open'] * tesla ['Volume']
toyota['Total Traded'] = toyota ['Open'] * toyota ['Volume']
gm['Total Traded'] = gm ['Open'] * gm ['Volume']                                             


# In[48]:


#now showing head and it will add a column to the the table for Total Traded
tesla.head()


# In[49]:


toyota.head()


# In[50]:


gm.head()


# In[51]:


# This will plot the total amount of trade for each company
#Comparing the total trade for each of the companies and create the plot
tesla['Total Traded'].plot(label='Tesla',figsize=(17,10))
toyota['Total Traded'].plot(label='Toyota')
gm['Total Traded'].plot(label='GM')
plt.ylabel('Total Traded')
plt.title('Total Trade for Tesla, GM and Toyota')
plt.legend() # To put a legend for it
plt.show()


# In[52]:


# to get the max for Tesla Traded
tesla['Total Traded'].argmax()


# In[53]:


# to get the max for Toyota Traded
toyota['Total Traded'].argmax()


# In[54]:


# to get the max for GM Traded
gm['Total Traded'].argmax()


# In[55]:


# using iLoc to find the date for the max total trade for Tesla
tesla.iloc[[tesla['Total Traded'].argmax()]]


# In[58]:


# using iLoc to find the date for the max total trade for Tesla
toyota.iloc[[toyota['Total Traded'].argmax()]]


# In[57]:


# using iLoc to find the date for the max total trade for Tesla
gm.iloc[[gm['Total Traded'].argmax()]]


# In[60]:


# Creating a moving average to make data more robust
# This will compare the open price using basic plot and the moving average of 50 and 100 for Tesla
tesla['Open'].plot(label='Tesla Original with no Moving Average',figsize=(17,10))
tesla['MA50'] = tesla['Open'].rolling(50).mean()
tesla['MA50'].plot(label = 'MA50')
tesla['MA100'] = tesla['Open'].rolling(100).mean()
tesla['MA100'].plot(label = 'MA100')
plt.ylabel('Open Prices for Tesla')
plt.title('Comparing using moving Average')
plt.legend() # To put a legend for it
plt.show()           


# In[62]:


from pandas.plotting import scatter_matrix
import pandas as pd


# In[64]:


car_comp = pd.concat([tesla['Open'],toyota['Open'],gm['Open']],axis=1)
car_comp.columns = ['Tesla Open', 'GM Open', 'Toyota Open']


# In[66]:


#creating Scatter matrix
scatter_matrix(car_comp,figsize=(10,10), hist_kwds={'bins' : 50})


# In[ ]:





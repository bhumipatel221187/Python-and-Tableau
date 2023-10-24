#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import the pandas libraries
import pandas as pd


# In[3]:


# import Zipfile library (use this to extract the file downloaed from kaggle)
import zipfile


# In[5]:


# import kaggle library (We wil use this to downloard the dataset programatically from kaggle)
import kaggle


# In[6]:


kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset


# In[7]:


import opendatasets as od


# In[8]:


get_ipython().system('pip install kaggle')


# In[9]:


import kaggle


# In[10]:


chmod 600 / home/mochen/.kaggle.json


# In[11]:


get_ipython().system('pip install opendatasets')


# In[12]:


import opendatasets as od


# In[13]:


dataset = 'https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset'


# In[14]:


od.download(dataset)


# In[15]:


import os


# In[16]:


data_dir = '.\london-bike-sharing-dataset'


# In[17]:


os.listdir(data_dir)


# In[18]:


bikes = pd.read_csv("london_merged.csv")


# In[19]:


import pandas as pd


# In[20]:


bikes = pd.read_csv('london_merged.csv')


# In[21]:


bikes


# In[22]:


bikes.info()


# In[23]:


bikes.shape


# In[24]:


# count the unique values in the weather_code column
bikes.weather_code.value_counts()


# In[25]:


# count the unique values in the season column
bikes.season.value_counts()


# In[26]:


# specifying the colum names that I want to use
new_cols_dict = {
    'timestamp':'time',
    'cnt':'count',
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}


# In[27]:


# Renaming the column to the specified column names
bikes.rename(new_cols_dict, axis=1, inplace=True)


# In[28]:


# changing the humadity values to percentage (i.e a value between 0 and 1)
bikes.humidity_percent = bikes.humidity_percent / 100


# In[29]:


# Creating a season dictionary so that we can map the integers 0-3 to the actual written values.
season_dict = {
    '0.0':'Spring',
    '1.0':'Summer',
    '2.0':'Autumn',
    '3.0':'Winter'
}


# In[30]:


# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered Clouds',
    '3.0':'Broken Clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
}


# In[31]:


# Changing the seasons column data type to string
bikes.season = bikes.season.astype('str')


# In[32]:


# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)


# In[33]:


# Changing the weather column data type to string
bikes.weather = bikes.weather.astype('str')


# In[34]:


# mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dict)


# In[35]:


# Checking our dataframe to see if the mapping have worked
bikes.head()


# In[36]:


# writing the final dataframe to an excel file that we will use in our Tableau Visualisations. The file will be the 'london_bikes_final'
bikes.to_excel('london_bikes_final.xlsx',sheet_name='Data')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ## Weather Processing

# ### Import the necessary libraries

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import date, datetime, timedelta


# ### Import the dataset. Assign it to a variable called data

# In[2]:


path = r'./Downloads/weather_dataset.data'
data = pd.read_csv(path, sep='\s+')


# ### Write a function in order to fix date (this relate only to the year info) and apply it
# 

# In[3]:


#Let's first look at the dataset and check the types of columns.

data.head(5)


# In[4]:


data.dtypes


# In[5]:


#Now let's check if columns Yr, Mo, Dy contain values appropriate for dates.
#As we can notice, days are in a range from 1 to 31, which is typical of dates.
#Months are in a range from 1 to 12, which is typical of dates.
#And years are in a range from 61 to 78, which is completely fine.

data.describe()


# In[6]:


#Let's fix year info.

data['Yr'] = data['Yr'].apply(lambda x: x+1900)
data['Yr']


# In[7]:


#And check if everything is all right with the Yr column.
#The range is between 1961 and 1978 as was expected.

data['Yr'].describe()


# ### Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]

# In[8]:


data['Date'] = data['Yr'].astype(str) + '-' + data['Mo'].astype(str) + '-' + data['Dy'].astype(str)
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
datetime_index = pd.DatetimeIndex(data['Date'].values)
data = data.set_index(datetime_index)


# In[9]:


#Let's drop unnecessary columns.

data.drop(['Yr','Mo','Dy','Date'], axis=1,inplace=True)
data[:5]


# ### Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them

# In[10]:


#Let's replace all values which contain any characters except for digits with nans.

data.replace('[^0-9.]', np.nan, regex=True, inplace=True)
data[:5]


# In[11]:


#Now we can change the data type of the whole dataset for convenience.

data = data.astype('float')


# In[12]:


data.dtypes


# ### Compute how many values are missing for each location over the entire record

# In[13]:


#Fist, we can create a heatmap for a visual representation of the missing values.
#However, we barely see them on it. It means that there are a few missing values.

fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis');


# In[14]:


#Let's count missing values more precisely.

missing_values = data.isna().sum()
missing_values


# #### Compute how many non-missing values there are in total

# In[15]:


#DataFrame.count is used to count non-NA cells for each column or row.

data.count().sum()


# In[16]:


#Let's fill in missing values with the help of the Next Observation Carried Backward technique.

data = data.bfill()


# In[17]:


#Now let's check if missing values have been filled in.

data.isna().sum() 


# ### Calculate the mean windspeeds of the windspeeds over all the locations and all the times

# In[18]:


#Descriptive statistics show a strange behavior in column loc9.
#The mean value differs a lot from other columns.

data.describe()


# In[19]:


#Let's look for outliers.
#For this purpose, we take the max value of windspeed from another column.

data.query("loc9 > 42.54")


# In[20]:


#Let's drop a row with the outlier.

data = data.drop("1976-05-31")


# In[21]:


#Now data looks normal.

data.describe()


# In[22]:


#Let's calculate the mean windspeeds.

data.stack().mean()


# ### Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
# 

# In[23]:


loc_stats = data.agg(["min", "max", "mean", "std"], axis=0)
loc_stats


# ### Find the average windspeed in January for each location

# In[24]:


january_data = data[data.index.month == 1]
january_data.mean()


# ### Downsample the record to a yearly frequency for each location

# In[25]:


yearly_frequency = data.resample('Y').mean()
yearly_frequency[:5]


# ### Downsample the record to a monthly frequency for each location

# In[26]:


data_monthly = data.resample('M').mean()
data_monthly[:5]


# ### Downsample the record to a weekly frequency for each location

# In[27]:


weekly_frequency = data.resample('W').mean()
weekly_frequency[:5]


# ### Calculate the min, max and mean windspeeds and standard deviations of the windspeeds  across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks

# In[28]:


#Let's find out which day of the week is our starting date.
#It's Monday.

starting_date = datetime.strptime("1961-01-02", '%Y-%m-%d').date()
starting_date.weekday()


# In[29]:


#Let's find the end of the 21-week period.

ending_date = starting_date + timedelta(weeks=21)
ending_date


# In[30]:


weeks = data[starting_date : ending_date]

loc_stats_21week = weeks.resample('W-MON').agg(["min", "max", "mean", "std"], axis = 0)
loc_stats_21week[:5]


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


# In[4]:


df=pd.read_csv('dataset-1.csv')
df


# # Q-1 Car_Matrix_generation
# 

# In[37]:


ndf = df.pivot(index='id_1', columns='id_2',values ='car')
ndf = ndf.fillna(0)
ndf


# In[36]:


ndf.info()


# # Q-2 Car Type Count Calculation

# In[12]:


df


# In[16]:


conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
choices = ['low', 'medium', 'high']
df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=choices)
df


# # Calculate the count of occurrences for each `car_type` category and return the result as a dictionary. Sort the dictionary alphabetically based on keys
# 

# In[24]:


type_counts = df['car_type'].value_counts().to_dict()
sorted_type_counts = dict(sorted(type_counts.items()))

sorted_type_counts


# # Q-3 Bus Count Index Retrieval

# In[29]:


df


# In[32]:


mean_bus_value = df['bus'].mean()
bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()
bus_indexes.sort()
bus_indexes     


# In[33]:


df


# # Q-4 Route filtering

# In[38]:


route_avg_truck = df.groupby('route')['truck'].mean()
selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
selected_routes.sort()
selected_routes


# # Q-5 Matrix Value Modification

# In[52]:


ndf = ndf.applymap(lambda x: round(x * 0.75, 1) if x > 20 else round(x * 1.25, 1))
ndf


# # Q-6 Time check

# In[59]:


cdf= pd.read_csv('D:\python\Mapup assesment\datasets\dataset-2.csv')
cdf


# In[62]:


cdf['start_timestamp'] = pd.to_datetime(cdf['startDay'] + ' ' + cdf['startTime'])
cdf['end_timestamp'] = pd.to_datetime(cdf['endDay'] + ' ' + cdf['endTime'])
cdf['duration'] = cdf['end_timestamp'] - cdf['start_timestamp']
completeness_check = (
        (cdf['duration'] >= pd.Timedelta('1 day')) &  
        (cdf['start_timestamp'].dt.dayofweek == 0) & 
        (cdf['end_timestamp'].dt.dayofweek == 6) 
    )
completeness_result = cdf.groupby(['id', 'id_2'])['duration'].count().eq(1) | ~completeness_check.groupby(['id', 'id_2']).all()
completeness_result


# In[ ]:





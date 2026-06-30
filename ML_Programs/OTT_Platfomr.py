#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/ott_streaming_platform.csv"


# In[3]:


df = pd.read_csv(url)
df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.describe()


# In[10]:


df["SubscriptionPlan"].value_counts()


# In[11]:


df[(df["DeviceType"] == "Smart TV") & (df["Country"] == "India")]


# In[13]:


df[df["SeriesWatched"] > 7]


# In[ ]:


df[()]


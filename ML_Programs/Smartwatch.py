#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


url = "http://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/smartwatch_health_tracking.csv"


# In[3]:


df = pd.read_csv(url)
df


# In[9]:


df[df["Steps"] > 7000].shape


# In[13]:


df[df["HeartRate"] < 72].shape


# In[14]:


df[df["FitnessLevel"] == "Average"].shape


# In[20]:


df[(df["WaterIntake"]  > 2.2) & (df["WaterIntake"] <3.0)].shape


# In[21]:


df[(df["FitnessLevel"]  == "Excellent") & (df["Steps"] < 9000)]


# In[25]:


df.groupby("Gender") ["CaloriesBurned"].sum()


# In[ ]:





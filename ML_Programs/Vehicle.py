#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/vehicle_service_records.csv")

df


# In[4]:


df[(df["PaymentMethod"] == "UPI") & (df["VehicleType"] == "SUV")].shape


# In[12]:


df1 = df[df["ServiceCost"]>3000]
df1
df1.shape


# In[15]:


df3 = df1[df1["ServiceDuration"] > 2]
df3


# In[16]:


df3[df3["CustomerCity"] == "Delhi"]


# In[ ]:





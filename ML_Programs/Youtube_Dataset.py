#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/Youtube_Dataset.csv")

df.shape


# In[2]:


df.isnull()


# In[3]:


df.head()


# In[4]:


df.tail()


# In[6]:


cnames = df["Channel_Name"].unique()
print(cnames)


# In[7]:


len(cnames)


# In[9]:


df[(df["Views"] > 50000) & (df["Views"]< 80000)]


# In[10]:


df[(df["Comment_Count"] > 50) & (df["Comment_Count"]< 800)]


# In[26]:


import matplotlib.pyplot as plt

Avg_views = df.groupby("Channel_Name")["Views"].mean()
print(Avg_views)
plt.bar(Avg_views.index, Avg_views.values)

plt.title("Average Views on Each Channel")
plt.xlabel("Channel Names")
plt.ylabel("Average Views")

plt.xticks(rotation=45, ha="right")

plt.show()


# In[32]:


Avg_views = df.groupby("Channel_Name")["Views"].mean()


Top10_views = Avg_views.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(Top10_views.index, Top10_views.values, color = "orange")

plt.title("Top 10 Channels by Average Views")
plt.xlabel("Channel Names")
plt.ylabel("Average Views")

plt.xticks(rotation=45, ha="right")

plt.show()


# In[33]:


df = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/iot_dataset.csv")
df.head()


# In[ ]:





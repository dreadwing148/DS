#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 📊 Data Visualization

## 🤔 What is Data Visualization?

Data Visualization is the process of representing data using charts, graphs, and plots to understand information quickly and easily.

Instead of reading hundreds of rows, we can see patterns and insights visually.

---

## ❓ Why Do We Need Visualization?

Imagine a dataset with:

- 50 Creators
- 12 Columns
- Thousands of values

Finding answers from tables is difficult.

Visualization helps us:

✅ Understand data quickly

✅ Compare categories easily

✅ Identify trends

✅ Detect unusual values (Outliers)

✅ Make better decisions

---

## 🌍 Real-World Examples

### 📺 YouTube Studio

- Views
- Subscribers
- Watch Time

### 📸 Instagram Insights

- Reach
- Engagement
- Followers

### ⌚ Smart Watch Apps

- Steps
- Calories Burned
- Heart Rate

### 📈 Stock Market Apps

- Price Trends
- Trading Volume

---

## 💡 What Can Visualization Tell Us?

Using the Social Media Creator Analytics Dataset:

get_ipython().run_line_magic('pinfo', 'followers')
get_ipython().run_line_magic('pinfo', 'best')
get_ipython().run_line_magic('pinfo', 'engagement')
get_ipython().run_line_magic('pinfo', 'views')

---

## 📉 Common Charts

### 📈 Line Chart

Shows trends over time.

Example:
- Subscriber Growth
- Monthly Revenue

---

### 📊 Bar Chart

Compares categories.

Example:
- Followers by Category
- Views by Platform

---

### 🥧 Pie Chart

Shows percentages.

Example:
- Platform Share
- Content Category Share

---

### 📋 Histogram

Shows data distribution.

Example:
- Followers Distribution
- Views Distribution

---

### 🔵 Scatter Plot

Shows relationships.

Example:
- Followers vs Views
- Likes vs Comments

---

## 🤖 Why Is Visualization Important in Machine Learning?

Machine Learning starts with understanding data.

### ML Workflow

Dataset
⬇️

Data Cleaning
⬇️

Data Analysis
⬇️

📊 Data Visualization
⬇️

Machine Learning Model

---

## 🎯 Summary

Data Visualization helps us:

✅ Understand data faster

✅ Compare values easily

✅ Discover patterns

✅ Identify trends

✅ Detect outliers

✅ Support decision-making

**A good Data Analyst sees patterns.  
A good Visualization helps everyone see those patterns.**


# In[1]:


import matplotlib.pyplot as plt

followers = [1000, 2000, 3500, 5000]

plt.plot(followers)

plt.show()


# In[2]:


import matplotlib.pyplot as plt

followers = [1000, 2000, 3500, 5000]

plt.plot(followers)

plt.title("Follower Growth")

plt.xlabel("Months")

plt.ylabel("Followers")

plt.show()


# In[3]:


import pandas as pd

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)
df.head(2)


# In[4]:


import matplotlib.pyplot as plt

plt.plot(df["Followers"].head(20))

plt.show()


# In[5]:


plt.plot(df["CreatorID"].head(10), df["Followers"].head(10))

plt.show()


# In[19]:


plt.plot(df["CreatorID"].head(10), df["Followers"].head(10))

plt.title("Followers of First 10 Creators")

plt.show()


# In[7]:


plt.plot(df["CreatorID"].head(10), df["Followers"].head(10))

plt.title("Followers of First 10 Creators")

plt.xlabel("Creator ID")

plt.ylabel("Followers")

plt.show()


# In[8]:


plt.plot(df["CreatorID"].head(20), df["Followers"].head(20))

plt.grid()

plt.show()


# In[9]:


import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]

followers = [1000,1500,2500,4000,5500]

plt.plot(months, followers)

plt.title("Subscriber Growth")

plt.xlabel("Month")

plt.ylabel("Subscribers")

plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

plt.plot(
    df["CreatorID"].head(10),
    df["Followers"].head(10)
)

plt.title("Followers of First 10 Creators")

plt.xlabel("Creator")

plt.ylabel("Followers")

plt.show()


# In[11]:


plt.plot(
    df["CreatorID"].head(10),
    df["Followers"].head(10),
    marker="o"
)

plt.show()


# ## Line Styles

# In[12]:


plt.plot(
    df["CreatorID"].head(10),
    df["Followers"].head(10),
    linestyle="--"
)

plt.show()


# In[13]:


plt.plot(
    df["CreatorID"].head(10),
    df["Followers"].head(10),
    linestyle=":"
)

plt.show()


# ## Followers vs Average Views

# In[14]:


plt.plot(
    df["CreatorID"].head(10),
    df["Followers"].head(10),
    label="Followers"
)

plt.plot(
    df["CreatorID"].head(10),
    df["AvgViews"].head(10),
    label="Views"
)

plt.legend()

plt.show()


# ---
# ## Count Creators by Platform

# In[28]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

platform_counts = df["Platform"].value_counts()

print(platform_counts)

plt.bar(platform_counts.index, platform_counts.values)

plt.title("Number of Creators by Platform")
plt.xlabel("Platform")
plt.ylabel("Number of Creators")

plt.show()


# ## Average Followers by Content Category

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"
df = pd.read_csv(url)

followers = df.groupby("ContentCategory")["Followers"].mean()

plt.figure(figsize=(10, 5))
plt.bar(followers.index, followers.values)

plt.title("Average Followers by Category")
plt.xlabel("Content Category")
plt.ylabel("Average Followers")
plt.xticks(rotation=45)

plt.show()


# ## Average Engagement Rate by Country

# In[20]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

engagement = df.groupby("Country")["EngagementRate"].mean()

print(engagement)

plt.figure(figsize=(10, 5))
plt.bar(engagement.index, engagement.values)

plt.title("Average Engagement Rate by Country")
plt.xlabel("Country")
plt.ylabel("Engagement Rate (%)")

plt.xticks(rotation=45)

plt.show()


# ## Top 10 Creators by Followers

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

top_creators = df.sort_values("Followers",ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_creators["CreatorID"],top_creators["Followers"])

plt.title("Top 10 Creators by Followers")
plt.xlabel("Creator ID")
plt.ylabel("Followers")

plt.show()


# ## Followers vs Views Comparison

# In[56]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

data = df.head(15)

x = np.arange(len(data))
print(x)
width = 0.4

plt.figure(figsize=(20, 7))
bars1 = plt.bar(x - width/2,data["Followers"],width,label="Followers")

bars2 = plt.bar(x + width/2,data["AvgViews"],width,label="Views")

plt.xticks(x, data["CreatorID"])
plt.title("Followers vs AvgViews")
plt.xlabel("Creator ID")
plt.ylabel("Count")

plt.bar_label(bars1, padding=3)
plt.bar_label(bars2, padding=3)

plt.tight_layout()
plt.show()


# In[1]:


import matplotlib.pyplot as plt
import numpy as np

categories = ['Q1', 'Q2', 'Q3', 'Q4']
sales_2024 = [20, 34, 30, 35]
sales_2025 = [25, 32, 34, 20]
sales_2026 = [12, 28, 40, 45]

x = np.arange(len(categories))  
width = 0.25 

fig, ax = plt.subplots(figsize=(8, 5))

rects1 = ax.bar(x - width, sales_2024, width, label='2024', color='skyblue')
rects2 = ax.bar(x,         sales_2025, width, label='2025', color='orange')
rects3 = ax.bar(x + width, sales_2026, width, label='2026', color='lightgreen')

ax.set_xlabel('Quarters')
ax.set_ylabel('Sales')
ax.set_title('3-Year Sales Comparison')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

plt.tight_layout()
plt.show()


# In[21]:


import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Category 1': [12, 18, 15, 20],
    'Category 2': [10, 16, 14, 22],
    'Category 3': [8, 12, 11, 18],
    'Category 4': [18, 24, 19, 27]
}

df = pd.DataFrame(data, index=['Group A', 'Group B', 'Group C', 'Group D'])

df.plot(kind='bar', stacked=False, figsize=(10, 6))

plt.title("N-Category Combined Bar Chart")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.xticks(rotation=0)
plt.legend(title="Categories")
plt.tight_layout()


plt.show()


# In[22]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/ott_streaming_platform.csv"
df = pd.read_csv(url)

plot_data = df[['WatchHours', 'MoviesWatched', 'SeriesWatched']]

plot_data.plot(kind='bar', stacked=False, figsize=(12,6), color=['skyblue', 'orange', 'green'])

plt.xticks(range(len(df)), df['UserID'], rotation=45)

plt.title("OTT Streaming Activity by User")
plt.xlabel("User ID")
plt.ylabel("Values")
plt.legend(title="Metrics")
plt.tight_layout()

plt.show()


# In[ ]:





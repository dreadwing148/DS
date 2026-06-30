#!/usr/bin/env python
# coding: utf-8

# # Pandas in Python
# 
# ## 📌 What is Pandas?
# **Pandas** is an open-source Python library used for **data manipulation and analysis**.  
# It helps you work with structured data like tables (similar to Excel or SQL).
# 
# It provides two main data structures:
# - **Series** → 1D labeled array (like a single column)
# - **DataFrame** → 2D table with rows and columns
# 
# ---
# 
# ## 🎯 Why use Pandas?
# Pandas is popular because it makes data handling simple and powerful:
# 
# - 📊 Works with tabular data easily
# - ⚡ Fast and efficient for large datasets
# - 🧹 Helps clean and prepare data
# - 🔍 Supports filtering, sorting, and analysis
# - 📁 Reads/writes files like CSV, Excel, JSON, SQL
# - 🤖 Commonly used in data science and machine learning
# 
# ---
# 
# ## 🛠️ How to use Pandas?
# 
# ### 1. Install Pandas
# ```bash
# pip install pandas
# ```
# 
# ---

# # Load Library

# In[1]:


import pandas as pd


# # Load File - We use URL here

# In[2]:


url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/warehouse_inventory.csv"


# # Read csv file and check the head

# In[3]:


df = pd.read_csv(url)
df.head()


# # Read tail

# In[4]:


df.tail(10)


# # Find Shape

# In[5]:


df.shape


# # See Column names

# In[6]:


df.columns


# # Dataset Information

# In[7]:


df.info()


# # Statistical Summary

# In[8]:


df.describe()


# # Selecting One Column

# In[9]:


df["StockQuantity"]


# # Product Name and Price only.

# In[10]:


df[["ProductName","UnitPrice", "ItemID"]]


# # Filtering

# ## Products costing more than ₹5000

# In[11]:


df[df["UnitPrice"] > 5000]


# ## Products costing more than ₹5000 and ₹7500

# In[12]:


df[(df["UnitPrice"] > 5000) & (df["UnitPrice"] < 7500)]


# ## Show only Electronics products.

# In[13]:


df[df["Warehouse"] == "Mumbai"]


# ## Show only Electronics products and of one warehouse.

# In[14]:


df[(df["Category"] == "Electronics") & (df["Warehouse"] == "Kochi")]


# ## Show products from cheapest to costliest.

# In[15]:


df.sort_values("UnitPrice")


# ## Show products from highest price to lowest price.

# In[16]:


df.sort_values("UnitPrice",ascending=False)


# ## Which categories exist?

# In[17]:


df["Supplier"].unique()


# ## How many products are Electronics?

# In[18]:


df["Warehouse"].value_counts()


# ---

# ## Data Analysis
# ### Data Analysis is the process of examining data to find useful information, patterns, trends, and answers to questions.
# 
# Example:
# 
# A manager asks:
# 
# - Which product is most expensive?
# - Which warehouse has the most stock?
# - Which supplier provides the most products?
# 
# Using Pandas, we analyze the dataset and answer these questions.

# In[19]:


df["UnitPrice"].max()


# In[20]:


df["UnitPrice"].min()


# In[21]:


df["UnitPrice"].mean()


# In[22]:


df["UnitPrice"].median()


# In[23]:


df["StockQuantity"].sum()


# In[24]:


df["ProductName"].count()


# In[25]:


df["UnitPrice"].std()


# In[26]:


df.groupby("Category")["UnitPrice"].mean()


# In[27]:


df.groupby("Warehouse")["StockQuantity"].sum()


# In[28]:


df1 = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/food_delivery_orders.csv")
df1


# In[41]:


import pandas as pd

data = {
    "Username": [
        "travel_with_arun", "foodie_neha", "rahul_clicks", "fitness_anu",
        "tech_guru", "daily_quotes", "fashion_vibes", "gaming_world",
        "music_mani", "foodie_neha", "Travel_With_Arun", None,
        "fitness_anu_", "techguru", "fashion_vibes", "gaming_world",
        "music_mani", "wanderlust_sara", "photo_king", "food_master"
    ],

    "Full_Name": [
        "Arun Kumar", "Neha Sharma", "Rahul Verma", "Anu Joseph",
        "Rohit Nair", "Quote Factory", "Priya Menon", "Game Hub",
        "Manikandan P", "Neha Sharma", "Arun Kumar", "Unknown",
        "Anu Joseph", "Rohit Nair", "Priya Menon", "Game Hub",
        "Manikandan P", "Sara Ali", "King Photography", None
    ],

    "Followers": [
        12500, 8500, 15000, 22000,
        45000, None, 18000, 35000,
        12000, 8500, 12500, 5000,
        22000, 47000, 18000, 35000,
        -100, 92000, 5000000, 6500
    ],

    "Following": [
        950, 1200, 780, 500,
        300, 100, None, 150,
        400, 1200, 950, 800,
        500, 320, None, 150,
        450, 700, 1200, ""
    ],

    "Posts": [
        320, 180, 250, 410,
        150, 600, 290, 520,
        None, 180, 320, 90,
        410, 155, 290, 520,
        220, 890, 10000, -5
    ],

    "Category": [
        "Travel", "Food", "Photography", "Fitness",
        "Technology", "Motivation", "Fashion", "Gaming",
        "Music", "Food", "travel", None,
        "Fitness", "Tech", "Fashion", "gaming",
        "Music", "Travel", "Photography", "Food"
    ],

    "Avg_Likes": [
        1500, 900, 1200, 2500,
        4000, 700, 1800, 3200,
        None, 900, 1500, 500,
        2500, 4100, 1800, 3200,
        1100, 8500, 250000, -50
    ],

    "Engagement_Rate": [
        "3.5%", "4.2%", "2.8%", "5.1%",
        "6.5%", "2.0%", "4.8%", "5.5%",
        None, "4.2%", "3.5%", "2.5%",
        "5.1%", "6.4%", "4.8%", "5.5%",
        "3.1%", "7.2%", "10.5%", "abc"
    ],

    "Country": [
        "India", "India", "India", "India",
        "India", "India", "India", "India",
        "India", "India", "india", None,
        "India", "India", "INDIA", "India",
        "India", "UAE", "India", "India"
    ],

    "Account_Created": [
        "2020-01-15", "2019-03-22", "2021-07-10", "2018-06-05",
        "2017-11-01", "2016-08-19", "2020-09-25", "2019-12-11",
        "2022-02-14", "2019-03-22", "2020-01-15", "",
        "2018-06-05", "2017-11-01", "2020-09-25", "2019-12-11",
        "2022-02-14", "2018-04-20", "2015-01-01", "invalid_date"
    ]
}

df = pd.DataFrame(data)

print("Original Data")
df.to_csv('output.csv', index=False)


# In[42]:


print("\nMissing Values")
df.isnull()



# In[43]:


print("\nMissing Values Count")
print(df.isnull().sum())


# In[44]:


df_filled = df.fillna({
    "Username": "Unknown",
    "Age": 0,
    "Followers": df["Followers"].mean(),
    
})

print("\nAfter fillna()")
print(df_filled)


# In[45]:


df_no_missing = df.dropna()

print("\nAfter dropna()")
print(df_no_missing)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ### Import Modules

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


# ### Load Dataset

# In[2]:


url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/flipkart_sales_enriched.csv"

df = pd.read_csv(url)

print("First 5 Records\n")
print(df.head())


# ### Select Features

# In[3]:


X = df[
    [
        "Price (INR)",
        "Customer Rating"
    ]
]


# ### Create K-Means Model

# In[4]:


model = KMeans(
    n_clusters=3,
    random_state=42
)


# ### Train Model

# In[5]:


model.fit(X)


# ### Assign Cluster

# In[6]:


df["Cluster"] = model.labels_

print("\nClustered Dataset\n")
print(df.head(10))


# ### Display Cluster Centers

# In[7]:


print("\nCluster Centers\n")
print(pd.DataFrame(model.cluster_centers_, columns=["Price (INR)", "Customer Rating"]))


# ### Predict New Product

# In[8]:


new_product = [[25000, 4.5]]

prediction = model.predict(new_product)
print("\nPredicted Cluster :", prediction[0])


# ### Scatter Plot

# In[9]:


plt.figure(figsize=(8,6))
plt.scatter(df["Price (INR)"], df["Customer Rating"], c=df["Cluster"],s=40)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], marker="X", s=250,
            label="Centroids"
)
plt.title("Flipkart Product Clustering")
plt.xlabel("Price (INR)")
plt.ylabel("Customer Rating")

plt.legend()

plt.show()


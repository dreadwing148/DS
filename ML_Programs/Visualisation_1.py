#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

plt.hist(df["Followers"])

plt.title("Distribution of Followers")
plt.xlabel("Followers")
plt.ylabel("Number of Creators")

plt.show()


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

plt.hist(df["AvgViews"], bins=50)

plt.title("Distribution of Average Views")
plt.xlabel("Average Views")
plt.ylabel("Number of Creators")

plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

plt.hist(df["AvgLikes"], bins=10)

plt.title("Distribution of Average Likes")
plt.xlabel("Average Likes")
plt.ylabel("Number of Creators")

plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

plt.hist(df["PostsPublished"], bins=6)

plt.title("Distribution of Posts Published")
plt.xlabel("Number of Posts")
plt.ylabel("Number of Creators")

plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

plt.hist(df["EngagementRate"], bins=7)

plt.title("Distribution of Engagement Rate")
plt.xlabel("Engagement Rate (%)")
plt.ylabel("Number of Creators")

plt.show()


# In[12]:





# In[16]:


import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/social_media_creator_analytics.csv"

df = pd.read_csv(url)

plt.hist(df["Followers"], bins=100)

plt.title("Followers Distribution (5 Bins)")
plt.xlabel("Followers")
plt.ylabel("Number of Creators")

plt.show()


# In[ ]:





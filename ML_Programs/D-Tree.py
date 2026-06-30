#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt


# # Step 1: Load dataset

# In[2]:


url = "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/loan_approval_dataset.csv"
df = pd.read_csv(url)


# # Step 2: Clean column names (remove leading/trailing spaces)

# In[3]:


df.columns = df.columns.str.strip()


# # Step 3: Encode categorical columns and display value

# In[4]:


for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        le.fit(df[col])   # learn mapping
        print(f"Encoding for {col}:")
        for i, cls in enumerate(le.classes_):
            print(f"  {cls} → {i}")
        print()
        df[col] = le.transform(df[col])  # apply encoding


# ### Step 4: Define features (X) and target (y)

# In[5]:


X = df.drop(['loan_id', 'loan_status'], axis=1)
y = df['loan_status']


# ### Step 5: Train/test split

# In[6]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# ### Step 6: Train Decision Tree

# In[7]:


model = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=42)
model.fit(X_train, y_train)


# ### Step 7: Predictions on test set

# In[8]:


y_pred = model.predict(X_test)


# ### Step 8: Evaluation

# In[9]:


print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nAccuracy:", accuracy_score(y_test, y_pred))


# # Step 9: Visualize the tree

# In[10]:


plt.figure(figsize=(20,10))
tree.plot_tree(model, feature_names=X.columns, class_names=model.classes_.astype(str), filled=True)
plt.show()


# # Step 10: Predict on new applicant

# In[11]:


new_applicant = {
    'no_of_dependents': 2,
    'education': 1,          # encoded value
    'self_employed': 0,      # 0 = No, 1 = Yes
    'income_annum': 500000,
    'loan_amount': 200000,
    'loan_term': 12,
    'cibil_score': 750,
    'residential_assets_value': 1000000,
    'commercial_assets_value': 0,
    'luxury_assets_value': 0,
    'bank_asset_value': 500000
}

applicant_df = pd.DataFrame([new_applicant])
prediction = model.predict(applicant_df)


# # Map numeric prediction back to labels

# In[12]:


label_map = {0: "Rejected", 1: "Approved"}
print("Predicted Loan Status:", label_map[prediction[0]])


# In[13]:


joblib.dump(model, "loan_model.pkl")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # 1. Import Libraries

# In[1]:


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# # 2. Load Dataset

# In[2]:


df = pd.read_csv(
    "https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/iot_smart_factory_sensors.csv"
)

print("First 5 Records\n")
df.head()


# # Label Encoding

# In[3]:


shift_encoder = LabelEncoder()
location_encoder = LabelEncoder()
status_encoder = LabelEncoder()

df["Shift"] = shift_encoder.fit_transform(df["Shift"])
df["FactoryLocation"] = location_encoder.fit_transform(df["FactoryLocation"])
df["MachineStatus"] = status_encoder.fit_transform(df["MachineStatus"])


# # Display Encoded Values

# In[4]:


print("\nMachine Status Mapping")

mapping = dict(
    zip(
        status_encoder.classes_,
        status_encoder.transform(status_encoder.classes_)
    )
)

print(mapping)


# # Features and Target

# In[5]:


X = df[
    [
        "Temperature",
        "Humidity",
        "Pressure",
        "Vibration",
        "PowerConsumption",
        "Shift",
        "FactoryLocation"
    ]
]

y = df["MachineStatus"]


# # Train-Test Split

# In[6]:


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# # Create and Train a Logistic Regression Model

# In[7]:


model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("\nModel Trained Successfully")


# # Predict and Comapre Actual vs Predicted

# In[8]:


predictions = model.predict(X_test)

result = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\nActual vs Predicted\n")
print(result.head(20))


# # Find Accuracy

# In[9]:


accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy :", accuracy)


# # Confusion Matrix

# In[10]:


print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, predictions))


# # Classification Report

# In[11]:


print("\nClassification Report\n")

print(classification_report(y_test, predictions))


# # Predict New Machine

# In[12]:


new_machine = [[
    46.5,      # Temperature
    61,        # Humidity
    101.3,     # Pressure
    2.4,       # Vibration
    128,       # Power Consumption
    1,         # Shift
    2          # Factory Location
]]
prediction = model.predict(new_machine)
status = status_encoder.inverse_transform(prediction)
print("\nPredicted Machine Status:")
print(status[0])


# # Prediction Probability

# In[13]:


probability = model.predict_proba(new_machine)
print("\nPrediction Probabilities")
for cls, prob in zip(status_encoder.classes_, probability[0]):
    print(f"{cls:15} : {prob:.4f}")


# In[20]:


df = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/employee_attrition.csv")
df


# In[ ]:





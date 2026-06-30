#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/iot_smart_factory_sensors.csv")

# Encode categorical columns
shift_encoder = LabelEncoder()
location_encoder = LabelEncoder()
status_encoder = LabelEncoder()

df["Shift"] = shift_encoder.fit_transform(df["Shift"])
df["FactoryLocation"] = location_encoder.fit_transform(df["FactoryLocation"])
df["MachineStatus"] = status_encoder.fit_transform(df["MachineStatus"])

# Features and Target
X = df.drop(["MachineID", "MachineStatus"], axis=1)
y = df["MachineStatus"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = LogisticRegression(max_iter=1000)

# Train Model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy :", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Predict New Machine
new_machine = [[46.5, 61, 101.3, 2.4, 128, 505, 1, 0]]

prediction = model.predict(new_machine)

print("\nPredicted Machine Status:")
print(status_encoder.inverse_transform(prediction))


# In[3]:


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/iot_smart_factory_sensors.csv")

# Encode categorical columns
shift_encoder = LabelEncoder()
location_encoder = LabelEncoder()
status_encoder = LabelEncoder()

df["Shift"] = shift_encoder.fit_transform(df["Shift"])
df["FactoryLocation"] = location_encoder.fit_transform(df["FactoryLocation"])
df["MachineStatus"] = status_encoder.fit_transform(df["MachineStatus"])

# Features and Target
X = df.drop(["MachineID", "ProductionUnits"], axis=1)
y = df["ProductionUnits"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("Mean Absolute Error :", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error :", mean_squared_error(y_test, y_pred))
print("R2 Score :", r2_score(y_test, y_pred))

# Predict Production Units
new_machine = [[46.5, 61, 101.3, 2.4, 128, 1, 0, 1]]

prediction = model.predict(new_machine)

print("\nPredicted Production Units:")
print(prediction[0])


# In[ ]:





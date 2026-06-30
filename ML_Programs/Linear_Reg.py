#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# # Polynomial Regression

# In[2]:


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

df = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/iot_smart_factory_sensors.csv")

# ----------------------------------------------------
# Encode Categorical Columns
# ----------------------------------------------------

shift_encoder = LabelEncoder()
location_encoder = LabelEncoder()
status_encoder = LabelEncoder()

df["Shift"] = shift_encoder.fit_transform(df["Shift"])
df["FactoryLocation"] = location_encoder.fit_transform(df["FactoryLocation"])
df["MachineStatus"] = status_encoder.fit_transform(df["MachineStatus"])

# ----------------------------------------------------
# Select Features
# ----------------------------------------------------

X = df[
    [
        "Temperature",
        "Humidity",
        "Pressure",
        "Vibration",
        "PowerConsumption",
        "Shift",
        "FactoryLocation",
        "MachineStatus"
    ]
]

# ----------------------------------------------------
# Select Target
# ----------------------------------------------------

y = df["ProductionUnits"]

# ----------------------------------------------------
# Convert Features into Polynomial Features
# ----------------------------------------------------

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)

# ----------------------------------------------------
# Train-Test Split
# ----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_poly,
    y,
    test_size=0.20,
    random_state=42
)

# ----------------------------------------------------
# Create Model
# ----------------------------------------------------

model = LinearRegression()

# ----------------------------------------------------
# Train Model
# ----------------------------------------------------

model.fit(X_train, y_train)

# ----------------------------------------------------
# Prediction
# ----------------------------------------------------

y_pred = model.predict(X_test)

# ----------------------------------------------------
# Compare Actual and Predicted
# ----------------------------------------------------

result = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print(result.head(20))

# ----------------------------------------------------
# Evaluation
# ----------------------------------------------------

print("\nMean Absolute Error :", mean_absolute_error(y_test, y_pred))

print("Mean Squared Error :", mean_squared_error(y_test, y_pred))

print("R2 Score :", r2_score(y_test, y_pred))

# ----------------------------------------------------
# Predict New Machine
# ----------------------------------------------------

new_machine = pd.DataFrame(
    [[46.5,61,101.3,2.4,128,1,0,1]],
    columns=[
        "Temperature",
        "Humidity",
        "Pressure",
        "Vibration",
        "PowerConsumption",
        "Shift",
        "FactoryLocation",
        "MachineStatus"
    ]
)

new_machine_poly = poly.transform(new_machine)

prediction = model.predict(new_machine_poly)

print("\nPredicted Production Units :")

print(prediction[0])


# In[ ]:





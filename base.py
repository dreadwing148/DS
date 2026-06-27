import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------
df = pd.read_csv("https://raw.githubusercontent.com/dreadwing148/DS/refs/heads/main/smartwatch_health_data.csv")

# ----------------------------------------------------
# Display First 5 Records
# ----------------------------------------------------
print("First 5 Records")
print(df.head())

# ----------------------------------------------------
# Data Cleaning
# ----------------------------------------------------
df["Activity Level"] = df["Activity Level"].replace({
    "Highly_Active": "Highly Active",
    "Actve": "Active",
    "Sedentary": "Seddentary"
    
})

df["Activity Level"] = df["Activity Level"].replace({
    "Seddentary": 1,
    "Active": 3,
    "Highly Active": 7,
})

df["Stress Level"] = df["Stress Level"].replace({
    "Very High" : 20
})
# ----------------------------------------------------
# Select Features (Independent Variables)
# ----------------------------------------------------
X = df[
    [
        "Heart Rate (BPM)",
        "Blood Oxygen Level (%)",
        "Step Count",
        "Sleep Duration (hours)"
    ]
]

# ----------------------------------------------------
# Select Target (Dependent Variable)
# ----------------------------------------------------
y = df["Stress Level"]

# ----------------------------------------------------
# Split Dataset
# ----------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Records :", len(X_train))
print("Testing Records  :", len(X_test))

# ----------------------------------------------------
# Create Linear Regression Model
# ----------------------------------------------------
model = LinearRegression()

# ----------------------------------------------------
# Train Model
# ----------------------------------------------------
model.fit(X_train, y_train)

print("\nModel Trained Successfully")

# ----------------------------------------------------
# Make Predictions
# ----------------------------------------------------
predictions = model.predict(X_test)

# ----------------------------------------------------
# Compare Actual vs Predicted
# ----------------------------------------------------
result = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\nActual vs Predicted")
print(result.head(20))

# ----------------------------------------------------
# Model Score (R² Score)
# ----------------------------------------------------
score = model.score(X_test, y_test)

print("\nR² Score :", score)

# ----------------------------------------------------
# Model Coefficients
# ----------------------------------------------------
print("\nIntercept :", model.intercept_)

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\nFeature Coefficients")
print(coefficients)

# ----------------------------------------------------
# Predict New Data
# ----------------------------------------------------
new_user = [[72, 98.4, 8500, 7.5]]

prediction = model.predict(new_user)

print("\nPredicted Stress Level :", prediction[0])

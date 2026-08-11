import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("../dataset/water_usage.csv")

# Convert Presence column to numbers
data["Presence"] = data["Presence"].map({"Yes": 1, "No": 0})

# Convert Result column to numbers
data["Result"] = data["Result"].map({"Normal": 0, "Wastage": 1})

# Inputs and Output
X = data[["FlowRate", "Duration", "Presence"]]
y = data["Result"]

# Train AI model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save trained model
joblib.dump(model, "water_model.pkl")

print("✅ AI DropGuard Model Trained Successfully!")
import os
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Find Dataset path automatically
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(
    base_path,
    "Dataset",
    "Water_usage.csv"
)

# Load dataset
data = pd.read_csv(dataset_path)

print("Dataset Loaded Successfully!")
print(data.head())


# Features and target
X = data[["Flow_Rate", "Duration", "Presence"]]
y = data["Wastage"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create and train model
model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)


# Check accuracy
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy)


# Save model inside Models folder
model_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "water_model.pkl"
)

with open(model_path, "wb") as file:
    pickle.dump(model, file)


print("AI DropGuard Model Saved Successfully!")
import os
import pickle


# Find model automatically
model_path = os.path.join(
    os.path.dirname(__file__),
    "Models",
    "water_model.pkl"
)

# Load AI model
with open(model_path, "rb") as file:
    model = pickle.load(file)


print("=== AI DropGuard Prediction ===")


try:
    flow = float(input("Enter Flow Rate: "))
    duration = float(input("Enter Duration: "))
    presence = input("Presence (Yes/No): ")

    # Convert Yes/No into numbers
    if presence.lower() == "yes":
        presence = 1
    else:
        presence = 0

    # Prediction
    result = model.predict([[flow, duration, presence]])

    if result[0] == 1:
        print("⚠️ Water Wastage Detected!")
    else:
        print("✅ Water Usage is Normal.")

except KeyboardInterrupt:
    print("\nPrediction stopped.")

except ValueError:
    print("Please enter valid numbers for Flow Rate and Duration.")
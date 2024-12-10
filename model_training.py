import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

# Load the cleaned dataset
data = pd.read_csv("./dataset/crop_recommendation_cleaned.csv")

# Debugging: Print column names to check if "Crop" exists
print("Columns in Dataset:", data.columns)

# Split features (X) and target (y)
X = data.drop("Crop", axis=1)
y = data["Crop"]

# Encode the target variable (Crop) using LabelEncoder
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model and label encoder
joblib.dump(model, "crop_recommendation_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

# Check accuracy on the test set
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

print("Model and encoder saved successfully!")

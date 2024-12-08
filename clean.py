import pandas as pd

# Load the original dataset
data = pd.read_csv("./dataset/crop_recommendation.csv")

# Print the first few rows to inspect the data
print("Original Dataset:")
print(data.head())

# Check for missing values and remove rows with missing values
print("Missing Values in Dataset:")
print(data.isnull().sum())

# Drop rows with missing values
data_cleaned = data.dropna()

# Ensure all columns have the correct data types
data_cleaned = data_cleaned.astype({
    "Nitrogen": "float",
    "Phosphorus": "float",
    "Potassium": "float",
    "Temperature": "float",
    "Humidity": "float",
    "pH": "float",
    "Rainfall": "float",
    "Crop": "str"
})

# Verify that data types are correct
print("Data Types After Cleaning:")
print(data_cleaned.dtypes)

# Save the cleaned dataset to a new CSV file
data_cleaned.to_csv("./dataset/crop_recommendation_cleaned.csv", index=False)

print("Cleaned Dataset Saved as 'crop_recommendation_cleaned.csv'!")

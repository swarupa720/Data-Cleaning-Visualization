
import pandas as pd
import os

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


data_folder = os.path.join(project_folder, "data")
csv_files = [f for f in os.listdir(data_folder) if f.lower().endswith(".csv")]

if not csv_files:
    print("No CSV file found in the data folder.")
else:
    file_path = os.path.join(data_folder, csv_files[0])
    df = pd.read_csv(file_path)

    print("Dataset loaded successfully!")
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nDataset information:")
    df.info()

    print("\nMissing values in each column:")
    print(df.isnull().sum())

    
# Step 8: Data quality check

print("\n--- DATA QUALITY REPORT ---")

# 1. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 2. Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# 3. Check dataset dimensions
print("\nNumber of rows and columns:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 4. Check data types
print("\nColumn data types:")
print(df.dtypes)

# 5. Display statistical summary
print("\nStatistical summary:")
print(df.describe(include="all"))

# Step 9: Clean the dataset

print("\n--- DATA CLEANING ---")

# Remove duplicate rows
df = df.drop_duplicates()
print("Duplicate rows removed.")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text values
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# Save the cleaned dataset in the project folder
output_folder = os.path.join(project_folder, "cleaned_data")
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(output_folder, "cleaned_dataset.csv")
df.to_csv(output_path, index=False)

print("Cleaned dataset saved successfully!")
print("Saved at:", output_path)
print("Final dataset shape:", df.shape)

# Step 10: Handle missing values

print("\n--- HANDLING MISSING VALUES ---")

# Check missing values before cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing numerical values with the column median
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].median())

# Fill missing text values with "Unknown"
text_columns = df.select_dtypes(include=["object", "string"]).columns

for column in text_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna("Unknown")

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save the updated cleaned dataset
output_path = os.path.join(
    output_folder, "cleaned_dataset.csv"
)
df.to_csv(output_path, index=False)

print("\nMissing value handling completed!")
print("Updated dataset saved successfully.")
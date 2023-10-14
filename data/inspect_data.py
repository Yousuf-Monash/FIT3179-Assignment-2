import pandas as pd

# Load your data
url = "https://raw.githubusercontent.com/Yousuf-Monash/FIT3179-Assignment-2/main/data/Billionaires%20Statistics%20Dataset.csv"
df = pd.read_csv(url)

# Columns to check for issues
columns_to_check = ["finalWorth", "gdp_country", "life_expectancy_country", "gross_tertiary_education_enrollment", "population_country"]

# Check for missing values
missing_values = df[columns_to_check].isnull().sum()
print("Missing Values:")
print(missing_values)

# Check for non-numeric values
for column in columns_to_check:
    non_numeric = df[~df[column].apply(lambda x: pd.api.types.is_numeric_dtype(type(x)))]
    if not non_numeric.empty:
        print(f"\nNon-numeric values found in column: {column}")
        print(non_numeric[[column]])

# Check for zero values which might cause issues in divisions
zero_values = (df[columns_to_check] == 0).sum()
print("\nZero Values:")
print(zero_values)

# Check for negative values which might be inappropriate for certain columns
negative_values = (df[columns_to_check] < 0).sum()
print("\nNegative Values:")
print(negative_values)

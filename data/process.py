import pandas as pd

df = pd.read_csv('Billionaires Statistics Dataset.csv')

# Assuming df is your DataFrame
columns_to_convert = [
    "cpi_country", "cpi_change_country", "gdp_country",
    "gross_tertiary_education_enrollment", "gross_primary_education_enrollment_country",
    "life_expectancy_country", "tax_revenue_country_country", "total_tax_rate_country",
    "population_country", "latitude_country", "longitude_country"
]

# Convert columns to float, converting errors (non-convertible values) to NaN
df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce', downcast='float')

df.to_csv('Billionaires Statistics Dataset.csv', encoding='utf-8', header=True, index=False)


pd.set_option('display.max_columns', None)

# Load your data
# Replace 'your_data.csv' with your actual file path
df = pd.read_csv('Billionaires Statistics Dataset.csv')

# Get a quick overview of the dataset
print(df.head())  # Display the first few rows of the dataframe

# Get a summary of the numerical columns
print(df.describe())

# Get info about data types, non-null counts, and memory usage
print(df.info())

# Get the number of unique values in each column
print(df.nunique())

# Get the count of missing values in each column
print(df.isnull().sum())

import pandas as pd

df = pd.read_csv('Billionaires Statistics Dataset.csv')

# Select only numeric columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

# Compute the mean of numeric columns and fill NaN values only in those
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Write the DataFrame to a new CSV file
df.to_csv('Billionaires Statistics Dataset Copy2.csv', index=False)

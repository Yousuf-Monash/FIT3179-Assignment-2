import pandas as pd

# Load the dataset
sheet = "Billionaires Statistics Dataset copy.csv"
data = pd.read_csv(sheet)

# Ensure that 'finalWorth' and 'gdp_country' columns exist in the data
if 'finalWorth' in data.columns and 'gdp_country' in data.columns:
    # Multiply 'finalWorth' by 1 million
    data['finalWorth'] = data['finalWorth'] * 1_000_000
    
    # Remove dollar signs and commas from 'gdp_country', then convert to numerical format
    data['gdp_country'] = pd.to_numeric(data['gdp_country'].replace({'\$': '', ',': ''}, regex=True), errors='coerce')
    
    # Handle NaN values resulted from conversion errors as per your requirement
    # For example, you might fill NaN values with a placeholder or the mean GDP:
    # data['gdp_country'].fillna(data['gdp_country'].mean(), inplace=True)
    
    # Save the preprocessed data back to CSV if needed
    data.to_csv('preprocessed_billionaires_data.csv', index=False)
else:
    print("Columns 'finalWorth' and/or 'gdp_country' not found in the data.")

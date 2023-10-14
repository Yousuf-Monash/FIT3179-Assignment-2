import pandas as pd

# Load your data
url = "Billionaires Statistics Dataset.csv"
df = pd.read_csv(url)

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', date_format='iso')

# Optionally, save the JSON data to a file
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

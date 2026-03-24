import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

# Convert to text (with or without headers)
content = df.to_string(index=False)

# Write to TXT
with open('span-eng.txt', 'w') as f:
    f.write(content)   
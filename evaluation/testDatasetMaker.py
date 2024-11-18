import pandas as pd
import random
import os

# Define file paths
input_csv = "output.csv"
output_csv = "evalDataset.csv"

# Step 1: Read the CSV file
df = pd.read_csv(input_csv)

# Step 2: Randomly select 500 entries 
random_df = df.sample(n=500, random_state=42)

# Step 3: Add code content from the file paths
def read_code(file_path):
    """Read the content of a file, return empty string if file doesn't exist."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return ""

random_df['TestFileCode'] = random_df['TestFilePath'].apply(read_code)
random_df['ProductionFileCode'] = random_df['ProductionFilePath'].apply(read_code)

# Step 4: Write the resulting DataFrame to a new CSV
random_df.to_csv(output_csv, index=False)

print(f"Randomly selected 500 entries with code added saved to {output_csv}.")

import csv
import os
import requests

# Define the directory to save the downloaded files
save_dir = "downloaded_files"
os.makedirs(save_dir, exist_ok=True)

# Function to download a file
def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}. Error: {e}")

# Read the CSV file
with open('clean.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Prepare the paths for raw_test and raw_actual
        test_file_name = os.path.join(save_dir, f"{row['id']}_test.java")
        actual_file_name = os.path.join(save_dir, f"{row['id']}_actual.java")

        # Download raw_test and raw_actual files
        download_file(row['raw_test'], test_file_name)
        download_file(row['raw_actual'], actual_file_name)

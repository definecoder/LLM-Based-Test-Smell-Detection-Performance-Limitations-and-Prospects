import pandas as pd

# Load the original CSV file
original_csv = 'clean.csv'
data = pd.read_csv(original_csv)

# Define the new CSV file path
output_csv = 'raw_for_tsDetect.csv'

# Prepare the data for the new CSV file
records = []
for _, row in data.iterrows():
    # Generate appName as 'idProject + testCase'
    app_name = f"{row['id']}_{row['idProject']}_{row['testCase'].split('.')[-1]}"

    # Generate paths for the test and production files
    path_to_test_file = f"/Users/codermehraj/Documents/codes/thesis/code-test-pair-for-tsDetect/downloaded_files/{row['id']}_test.java"
    path_to_production_file = f"/Users/codermehraj/Documents/codes/thesis/code-test-pair-for-tsDetect/downloaded_files/{row['id']}_actual.java"

    # Append to records list
    records.append({
        'appName': app_name,
        'pathToTestFile': path_to_test_file,
        'pathToProductionFile': path_to_production_file
    })

# Create a DataFrame and save to CSV
new_df = pd.DataFrame(records)
new_df.to_csv(output_csv, index=False)

print(f"New CSV file created at {output_csv}")

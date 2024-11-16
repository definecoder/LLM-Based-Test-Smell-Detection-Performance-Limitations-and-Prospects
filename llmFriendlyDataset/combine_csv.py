# combine_csv.py
import pandas as pd
import os
from tqdm import tqdm

def combine_csv_files(input_dir="split_csv_output", output_file="combined_output.csv", prefix="split"):
    """
    Combine multiple CSV files into a single file
    
    Args:
        input_dir (str): Directory containing split CSV files
        output_file (str): Path for combined output file
        prefix (str): Prefix of split files to combine
    """
    print(f"Reading files from {input_dir}...")
    
    # Get all split CSV files
    files = [f for f in os.listdir(input_dir) if f.startswith(prefix) and f.endswith('.csv')]
    files.sort()  # Ensure files are processed in order
    
    # Read and combine all files
    dfs = []
    for file in tqdm(files, desc="Combining files"):
        file_path = os.path.join(input_dir, file)
        df = pd.read_csv(file_path)
        dfs.append(df)
    
    # Combine all dataframes
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Save combined file
    combined_df.to_csv(output_file, index=False)
    print(f"Created combined file {output_file} with {len(combined_df)} rows")

if __name__ == "__main__":
    combine_csv_files()

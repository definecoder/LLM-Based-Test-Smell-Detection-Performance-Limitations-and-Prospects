import pandas as pd
import math
import os

def split_csv(input_file, output_prefix, chunks=10):
    """
    Split a CSV file into smaller chunks
    
    Args:
        input_file (str): Path to input CSV
        output_prefix (str): Prefix for output files
        chunks (int): Number of files to split into
    """
    # Read the CSV
    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file)
    
    # Calculate rows per chunk
    total_rows = len(df)
    rows_per_chunk = math.ceil(total_rows / chunks)
    
    # Create output directory if it doesn't exist
    output_dir = "split_csv_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Split and save
    for i in range(chunks):
        start_idx = i * rows_per_chunk
        end_idx = min((i + 1) * rows_per_chunk, total_rows)
        
        # Extract chunk
        chunk = df[start_idx:end_idx]
        
        # Generate output filename
        output_file = os.path.join(output_dir, f"{output_prefix}_{i+1}.csv")
        
        # Save chunk
        chunk.to_csv(output_file, index=False)
        print(f"Created {output_file} with {len(chunk)} rows")

if __name__ == "__main__":
    # Example usage
    input_file = "output.csv"  # Change this to your input file
    output_prefix = "split"
    num_chunks = 10  # Change this to desired number of splits
    
    split_csv(input_file, output_prefix, num_chunks)
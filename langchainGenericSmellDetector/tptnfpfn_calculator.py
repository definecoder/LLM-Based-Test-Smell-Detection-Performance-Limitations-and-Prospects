import os
import pandas as pd

def create_metrics_summary(result_folder, output_file='metrics_summary.csv'):
    # Initialize list to store summaries
    summaries = []
    
    # Process each CSV file
    for filename in os.listdir(result_folder):
        if filename.endswith('.csv'):
            # Read CSV
            df = pd.read_csv(os.path.join(result_folder, filename))
            
            # Calculate sums
            summary = {
                'file_name': filename,
                'total_false_positive': df['false_positive'].sum(),
                'total_false_negative': df['false_negative'].sum(),
                'total_true_positive': df['true_positive'].sum(),
                'total_true_negative': df['true_negative'].sum()
            }
            
            summaries.append(summary)
    
    # Create summary DataFrame
    summary_df = pd.DataFrame(summaries)
    
    # Save to CSV
    summary_df.to_csv(output_file, index=False)
    print(f"Summary saved to {output_file}")
    
    return summary_df

summary = create_metrics_summary('result')
print(summary)
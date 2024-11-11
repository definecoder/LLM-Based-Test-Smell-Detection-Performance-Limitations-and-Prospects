from code_parser.testCodeParser import test_code_parser
import csv

def process_csv_and_load_files(csv_file_path):
    """Iterate over each entry in the CSV and load test and main files."""
    with open(csv_file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        
        n = 0
        
        for row in reader:
            test_file_url = row['raw_test']
            main_file_url = row['raw_actual']                        
            test_case = row['testCase']
            
            
            print(f"\nProcessing ID: {row['id']}")
            if n > 100:
                test_code_parser(test_file_url, main_file_url, test_case)                        
            
            n += 1
            
            if n == 111:
                break


process_csv_and_load_files('clean.csv')
from code_parser.testCodeParser import test_code_parser
import csv

def process_csv_and_load_files(csv_file_path):
    """Iterate over each entry in the CSV and load test and main files."""
    with open(csv_file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)   
        
        total_columns = 9074
        completed_columns = 0             
        
        for row in reader:                        
            test_file_url = row['raw_test']
            # main_file_url = row['raw_actual']                        
            test_case = row['testCase']
            id = row['id']
            
            isEagerTest = row['EagerTest']
            isMysteryGuest = row['MysteryGuest']
            isResourceOptimism = row['ResourceOptimism']
            isRedundent = row['TestRedundancy']
                        
            print(f"\nProcessing ID: {id}")            
            test_code_parser(test_file_url, test_case, isEagerTest, isMysteryGuest, isResourceOptimism, isRedundent)                        
            
            completed_columns += 1
            
            print(f"Completed {completed_columns} of {total_columns} columns. {round((completed_columns/total_columns)*100, 2)}%")            
            


process_csv_and_load_files('clean.csv')
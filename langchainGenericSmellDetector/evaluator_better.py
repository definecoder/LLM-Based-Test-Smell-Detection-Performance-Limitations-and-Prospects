import pandas as pd
import os
from huggingFaceAgent import detectSmell
from groqAgent import detectSmellWithGroq
import time

from huggingFaceMiddleware import smellSirializer

smell_columns = ['Assertion Roulette', 'Conditional Test Logic', 'Constructor Initialization',
                    'Default Test', 'EmptyTest', 'Exception Catching Throwing', 'General Fixture',
                    'Mystery Guest', 'Print Statement', 'Redundant Assertion', 'Sensitive Equality',
                    'Verbose Test', 'Wait And See', 'Eager Test', 'Lazy Test', 'Lazy Assert',
                    'Unknown Test']

def getSmellsByModel(test_code, prod_code):
    """
    Simulates model inference. Replace with actual API call.
    """
    # Example of dynamic model integration
    prod_code = ""

    smells  = smellSirializer(detectSmellWithGroq(test_code, prod_code))
    
    # return ['Assertion Roulette', 'Conditional Test Logic']
    return smells

def analyze_test_smells(row):
    app_name = row['App']
    TestFilePath = row['TestFilePath']
    ProductionFilePath = row['ProductionFilePath']
    test_file_content = row['TestFileCode']
    prod_file_content = row['ProductionFileCode']        

    present_smells = [smell for smell in smell_columns if row[smell] == True]
    # print(f"Analyzing test smells for found {len(present_smells)} smells")    
    found_smells = getSmellsByModel(test_file_content, prod_file_content)
    
    true_positive = len(set(present_smells).intersection(found_smells))
    false_positive = len(set(found_smells).difference(present_smells))
    false_negative = len(set(present_smells).difference(found_smells))
    true_negative = len(set(smell_columns) - set(present_smells) - set(found_smells))
    
    print("Test Smells: ", present_smells)
    print("Found Smells: ", found_smells)
    print(f"TP: {true_positive}, FP: {false_positive}, FN: {false_negative}, TN: {true_negative}")
    
    return {
        'App': app_name,
        'TestFilePath': TestFilePath,
        'ProductionFilePath': ProductionFilePath,
        'TestFileCode': test_file_content,
        'ProductionFileCode': prod_file_content,
        'present_smells': present_smells,
        'found_smells': found_smells,        
        'false_positive': false_positive,
        'false_negative': false_negative,
        'true_positive': true_positive,
        'true_negative': true_negative
    }

def calculate_metrics(results_df):
    tp = results_df['true_positive'].sum()
    fp = results_df['false_positive'].sum()
    fn = results_df['false_negative'].sum()
    tn = results_df['true_negative'].sum()
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = (tp + tn) / (tp + fp + fn + tn) if (tp + fp + fn + tn) > 0 else 0
    
    return precision, recall, f1_score, accuracy

def save_results(results_df, evaluation_name, precision, recall, f1_score, accuracy):
    os.makedirs('result', exist_ok=True)
    results_df.to_csv(f'result/evaluation_result_{evaluation_name}.csv', index=False)
    
    summary = {
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1_score,
        "Accuracy": accuracy
    }        
    
    with open(f'result/summary_{evaluation_name}.json', 'w') as file:
        import json
        json.dump(summary, file, indent=4)
    
    print(f"Results saved: evaluation_result_{evaluation_name}.csv and summary_{evaluation_name}.json")

def token_count(text):
    tokens = len(text)
    return tokens

def main():
    evaluation_name = 'mixtral-8x7b-32768-large'
    try:
        df = pd.read_csv('evalDataset.csv')
    except Exception as e:
        print(f"Error reading input file: {e}")
        return
    
    # n = 100  # or any number you want
    # df = df.head(n)

    required_columns = ['TestFileCode', 'ProductionFileCode'] + smell_columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in input data: {missing_columns}")
    
    df['tokens'] = df['TestFileCode'].apply(token_count)
    df = df.sort_values(by='tokens', ascending=False).reset_index(drop=True)
    
    n = 50
    df = df.head(n)
    
    print(f"Analyzing {len(df)} test files")    
        

    analysis_results = []
    for index, row in df.iterrows():
        print(f"Analyzing row {index}")
        try:
            result = analyze_test_smells(row)
            analysis_results.append(result)
            time.sleep(30)
        except Exception as e:
            print(f"Error analyzing row {index}: {e}")
            try:
                result = analyze_test_smells(row)
                analysis_results.append(result)
                time.sleep(30)
            except Exception as e:
                print(f"Error analyzing row {index} again: {e}")                            
                result = {
                    'App': row['App'],
                    'TestFilePath': row['TestFilePath'],
                    'ProductionFilePath': row['ProductionFilePath'],
                    'TestFileCode': row['TestFileCode'],
                    'ProductionFileCode': row['ProductionFileCode'],
                    'present_smells': [],
                    'found_smells': [],
                    'false_positive': 0,
                    'false_negative': 0,
                    'true_positive': 0,
                    'true_negative': 0
                }
                analysis_results.append(result)
                time.sleep(60)
                continue
    
    df['analysis'] = analysis_results
    results_df = pd.DataFrame(df['analysis'].tolist())

    precision, recall, f1_score, accuracy = calculate_metrics(results_df)
    save_results(results_df, evaluation_name, precision, recall, f1_score, accuracy)

if __name__ == "__main__":
    main()

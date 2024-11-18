import pandas as pd
import google.generativeai as genai
import os

smell_columns = ['Assertion Roulette', 'Conditional Test Logic', 'Constructor Initialization',
                    'Default Test', 'EmptyTest', 'Exception Catching Throwing', 'General Fixture',
                    'Mystery Guest', 'Print Statement', 'Redundant Assertion', 'Sensitive Equality',
                    'Verbose Test', 'Wait And See', 'Eager Test', 'Lazy Test', 'Lazy Assert',
                    'Unknown Test']

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except:
        return "Could not read file"

def getSmellsByModel():
    test_smells = [
        'Assertion Roulette', 'Conditional Test Logic', 'Constructor Initialization',
    ]        
    
    return test_smells

def analyze_test_smells(row):
    # test_file_content = read_file_content(row['TestFilePath'])
    # prod_file_content = read_file_content(row['ProductionFilePath'])
    
    test_file_content = row['TestFileCode']
    prod_file_content = row['ProductionFileCode']        

    # Get list of present test smells
    present_smells = [smell for smell in smell_columns if row[smell] == "true"]
    # smells_list = ", ".join(present_smells)        
    
    # Generate test smells using the method which needs to be tested
    found_smells = getSmellsByModel()
    
    # Return the analysis
    # True Positive (TP): The model correctly predicts positive.
    # False Positive (FP): The model wrongly predicts positive.
    # True Negative (TN): The model correctly predicts negative.
    # False Negative (FN): The model wrongly predicts negative.
    
    number_of_true_positives = len(set(present_smells).intersection(found_smells))
    number_of_false_positives = len(set(found_smells).difference(present_smells))
    number_of_true_negatives = len(set(smell_columns) - set(present_smells) - set(found_smells))
    number_of_false_negatives = len(present_smells) - number_of_true_positives
    
    return {        
        'false_positive': number_of_false_positives,
        'false_negative': number_of_false_negatives,
        'true_positive': number_of_true_positives,
        'true_negative': number_of_true_negatives, 
        'test_smells': present_smells,
        'found_smells': found_smells        
    }

def main():
    evaluation_name = 'gpt-4o-mini'
    df = pd.read_csv('evalDataset.csv')

    # Validate input data
    required_columns = ['TestFileCode', 'ProductionFileCode'] + smell_columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in input data: {missing_columns}")

    # Analyze each row
    df['analysis'] = df.apply(analyze_test_smells, axis=1)
    results_df = pd.DataFrame(df['analysis'].tolist())

    # Aggregate metrics
    total_tp = results_df['true_positive'].sum()
    total_fp = results_df['false_positive'].sum()
    total_fn = results_df['false_negative'].sum()
    total_tn = results_df['true_negative'].sum()

    precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = (total_tp + total_tn) / (total_tp + total_fp + total_fn + total_tn)

    # Save results
    os.makedirs('result', exist_ok=True)
    results_df.to_csv(f'result/evaluation_result_{evaluation_name}.csv', index=False)

    print(f"Analysis complete! Results saved to evaluation_result_{evaluation_name}.csv")
    print(f"Precision: {precision}, Recall: {recall}, F1 Score: {f1_score}, Accuracy: {accuracy}")

    
if __name__ == "__main__":
    main()
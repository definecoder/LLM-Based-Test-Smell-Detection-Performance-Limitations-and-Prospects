import pandas as pd

# Define the mapping for binary flags to labels
flags_map = {
    'isEagerTest': "Eager Test",
    'isMysteryGuest': "Mystery Guest",
    'isResourceOptimism': "Resource Optimism",
    'isRedundent': "Redundent Print"
}

# Convert binary indicators to labels
def interpret_flags(row):
    labels = []
    if row['isEagerTest'] == 1:
        labels.append(flags_map['isEagerTest'])
    if row['isMysteryGuest'] == 1:
        labels.append(flags_map['isMysteryGuest'])
    if row['isResourceOptimism'] == 1:
        labels.append(flags_map['isResourceOptimism'])
    if row['isRedundent'] == 1:
        labels.append(flags_map['isRedundent'])
    return ' + '.join(labels)

# Load the CSV file
data = pd.read_csv('all_smells.csv') 

import pandas as pd

# Define the mapping for binary flags to labels
flags_map = {
    'isEagerTest': "Eager Test",
    'isMysteryGuest': "Mystery Guest",
    'isResourceOptimism': "Resource Optimism",
    'isRedundent': "Redundent Print"
}

# Convert binary indicators to labels
def interpret_flags(row):
    labels = []
    if row['isEagerTest'] == 1:
        labels.append(flags_map['isEagerTest'])
    if row['isMysteryGuest'] == 1:
        labels.append(flags_map['isMysteryGuest'])
    if row['isResourceOptimism'] == 1:
        labels.append(flags_map['isResourceOptimism'])
    if row['isRedundent'] == 1:
        labels.append(flags_map['isRedundent'])
    
    if len(labels) == 0:
        return 'No Smells'
    else:
        return ' + '.join(labels)

# Load the CSV file
data = pd.read_csv('all_smells.csv')  # Replace with your actual file name

# Apply interpretation to each row and create a new column
data['detected_smells'] = data.apply(interpret_flags, axis=1)

# Drop the original binary flag columns
data = data.drop(columns=['isEagerTest', 'isMysteryGuest', 'isResourceOptimism', 'isRedundent'])

# Save the modified DataFrame to a new CSV
data.to_csv('all_smells_interpreted.csv', index=False)

print("CSV file saved as 'all_smells_interpreted.csv'")



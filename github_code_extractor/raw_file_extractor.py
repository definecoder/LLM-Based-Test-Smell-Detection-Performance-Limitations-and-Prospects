import re

def convert_to_raw_url(github_url):
    # Match the GitHub URL structure for a file in the repository
    try: 
        match = re.match(r'https://github.com/([^/]+)/([^/]+)/blob/([^/]+)/(.*)', github_url)
        
        if match:
            user, repo, branch, file_path = match.groups()
            raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{file_path}"
            return raw_url
        else:
            return "Invalid GitHub URL"
        
    except Exception as e:
        return f"URL: {github_url}\nError processing URL: {e}"

# Example usage
# url = "https://github.com/vmware-archive/admiral/blob/master/auth/src/test/java/com/vmware/admiral/auth/idm/PrincipalRolesHandlerTest.java"
# raw_url = convert_to_raw_url(url)
# print(raw_url)


# Generating raw URL for our clean dataset

import pandas as pd
from tqdm import tqdm

tqdm.pandas()

df = pd.read_csv('./resources/clean.csv')

print(df.iloc[0]['Actual Class'])

df['raw_test'] = df.progress_apply(
    lambda row: convert_to_raw_url(row['Test Class']),
    axis=1,
    result_type='expand'
)

df['raw_actual'] = df.progress_apply(
    lambda row: convert_to_raw_url(row['Actual Class']),
    axis=1,
    result_type='expand'
)


df.to_csv('./resources/clean_raw.csv', index=False)



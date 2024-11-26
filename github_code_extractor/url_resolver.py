import requests
import sys
import pandas as pd

def get_final_url(url):
    try:
        response = requests.get(url, allow_redirects=True)
        return response.url
    except Exception as e:
        print(f"Error processing URL '{url}': {e}")
        return None
    

def get_final_urls(urls):
    return [get_final_url(url) for url in urls]

# print(get_final_urls(["https://www.chat.com", "https://google.com"]))

# repo_df = pd.read_csv("../resources/projects_with_default_branch.csv")

raw_df = pd.read_csv("./resources/clean.csv")

output_file = "./resources/cleanv2.csv"

from tqdm import tqdm

# tqdm.pandas()

# repo_df['url'] = repo_df['url'].progress_apply(get_final_url)
# raw_df['raw_test'] = raw_df['raw_test'].progress_apply(get_final_url)

tqdm.pandas()

# raw_df['raw_actual'] = raw_df['raw_actual'].progress_apply(get_final_url)

# repo_df.to_csv("../resources/projects_with_final_url.csv", index=False)

# raw_df.to_csv(output_file, index=False)



try: 
    open(output_file, 'x').close()
    raw_df.iloc[:0].to_csv(output_file, index=False)
except FileExistsError:
    pass


num_chunks = 20
chunk_size = len(raw_df) // num_chunks


start_row = int(sys.argv[1]) if len(sys.argv) > 1 else 0

start_chunk = start_row // chunk_size



for i in range(start_chunk, num_chunks):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_chunks - 1 else len(raw_df)


    df_chunk = raw_df.iloc[start:end].copy()


    df_chunk[['raw_test', 'raw_actual']] = df_chunk.progress_apply(
        lambda row: get_final_urls([row['raw_test'], row['raw_actual']]),
        axis=1,
        result_type='expand'
    ) 

    df_chunk.to_csv(output_file, mode='a', header=False, index=False)

    print(f"Completed and saved chunk {i+1}/{num_chunks}")
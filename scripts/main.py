import pandas as pd
from dotenv import load_dotenv
import os
import time
from tqdm import tqdm
from search_script import search_endpoint

API_KEY = os.getenv("API_KEY")

# Number of results from a single API call
results_num = 1

# environment variable
load_dotenv() 

final_data_dict = []

def local_data(idx):
    sample_titles = pd.read_csv('../data/sample-titles.csv')
    titles_list = sample_titles.values.tolist()
    return titles_list[idx]

def main():

    sample_len = pd.read_csv('../data/sample-titles.csv')
    titles_len = sample_len.values.tolist()
    
    for num in tqdm(range(0, len(titles_len))):
        res = search_endpoint(API_KEY, local_data(num), results_num)
        final_data_dict.append(res)
       
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Completed in {end_time - start_time} seconds')
    print(final_data_dict)
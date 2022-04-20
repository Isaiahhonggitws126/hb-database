import pandas as pd
from dotenv import load_dotenv
import os
from search_script import search_endpoint

API_KEY = os.getenv("API_KEY")
results_num = 5

load_dotenv() 
# environment variable

final_data_dict = {
    'videoId': [],
    'channelId': [],
    'description': []
}

def local_data(idx):
    sample_titles = pd.read_csv('../data/sample-titles.csv')
    titles_list = sample_titles.values.tolist()
    return titles_list[idx]

def main():
    res = search_endpoint(API_KEY, local_data(1), results_num)
    print(res)

if __name__ == '__main__':
    main()
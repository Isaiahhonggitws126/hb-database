from lib2to3.pgen2.pgen import DFAState
from random import sample
from re import T
import requests
import json
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
from pathlib import Path
import time
import pandas as pd
from tqdm import tqdm

# environment variable
load_dotenv(Path("../.env")) 

# Calling the API with pyyoutube
API_KEY = os.getenv("API_KEY")

youtube = build('youtube', 'v3', developerKey=API_KEY)

sample_queries = pd.read_csv("../data/sample-titles.csv")

final_dict = {
    'channelId': [],
    'channelTitle': [],
}

def get_channel_id(API_KEY, df):

    for queries in tqdm(range(len(df))):
        time.sleep(1)
        try:
            # Search Endpoint
            url = f'https://www.googleapis.com/youtube/v3/search/?key={API_KEY}&part=snippet&max_results=1&q={df.loc[queries]}'
            json_url = requests.get(url)
            search_data = json.loads(json_url.text)
            final_dict['channelId'].append(search_data['items'][0]['snippet']['channelId'])
            final_dict['channelTitle'].append(search_data['items'][0]['snippet']['channelTitle'])

        except:
            print("Something went wrong.")

def main():
    get_channel_id(API_KEY, sample_queries)
    print(final_dict)
    

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Completed in {end_time - start_time} seconds')
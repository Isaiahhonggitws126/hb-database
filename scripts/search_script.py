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

# environment variable
load_dotenv(Path("../.env")) 

# Calling the API with pyyoutube
API_KEY = os.getenv("API_KEY")

youtube = build('youtube', 'v3', developerKey=API_KEY)

results_count = 2

titles_df = pd.read_csv("../data/sample-titles.csv")

def get_channel_id(API_KEY, df, results_num):
    
    for rows in df:
        try:
            # Search Endpoint
            url = f'https://www.googleapis.com/youtube/v3/search/?key={API_KEY}&part=snippet&max_results={results_num}&q={df[rows]}'
            json_url = requests.get(url)
            search_data = json.loads(json_url.text)
            return search_data['items'][0]['snippet']['channelId']

        except:
            print("Something went wrong.")

def main():
    print(get_channel_id(API_KEY, titles_df, results_count))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Completed in {end_time - start_time} seconds')
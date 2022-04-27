from random import sample
import re
import requests
import json
import os
import time
from dotenv import load_dotenv

load_dotenv() 
# environment variable

API_KEY = os.getenv("API_KEY")

def search_endpoint(API_KEY, title, results_num):
    try:
        time.sleep(2)
        url = f'https://www.googleapis.com/youtube/v3/search/?key={API_KEY}&part=snippet&max_results={results_num}&q={title}'
        json_url = requests.get(url)
        search_data = json.loads(json_url.text)
        return search_data['items'][0]['snippet']
            
    except:
        print("Something went wrong.")
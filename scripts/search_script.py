from random import sample
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv() 
# environment variable

API_KEY = os.getenv("API_KEY")

def search_endpoint(API_KEY, title, results_num):
    try:
        url = f'https://www.googleapis.com/youtube/v3/search/?key={API_KEY}&part=snippet&max_results={results_num}&q={title}'
        json_url = requests.get(url)
        search_data = json.loads(json_url.text)
        for i in range(0, len(search_data['items'])):
            return search_data['items'][i]
            
    except:
        print("Something went wrong.")
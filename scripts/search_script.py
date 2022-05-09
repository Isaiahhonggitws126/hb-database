from random import sample
import requests
import json
import os

def search_endpoint(API_KEY, title, results_num):
    try:
        url = f'https://www.googleapis.com/youtube/v3/search/?key={API_KEY}&part=snippet&max_results={results_num}&q={title}'
        json_url = requests.get(url)
        search_data = json.loads(json_url.text)
        return search_data
            
    except:
        print("Something went wrong.")



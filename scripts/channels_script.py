from random import sample
from numpy import True_
import requests
import json

def playlists_items_endpoint(API_KEY, upload_id, query_counts):
        url = f'https://www.googleapis.com/youtube/v3/playlistItems/?key={API_KEY}&part=snippet&playlistId={upload_id}&max_results={query_counts}'
        json_url = requests.get(url)
        playlist_response = json.loads(json_url.text)
        return playlist_response 
         
        
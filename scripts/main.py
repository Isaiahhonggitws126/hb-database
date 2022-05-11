from calendar import c
from textwrap import indent
from typing import final
import pandas as pd
from dotenv import load_dotenv
import os
import time
from pathlib import Path
import json
from googleapiclient.discovery import build

# environment variable
load_dotenv(Path("../.env")) 

# Calling the API with pyyoutube
API_KEY = os.getenv("API_KEY")

youtube = build('youtube', 'v3', developerKey=API_KEY)

# Number of results from a single API call
results_count = 50

def channel_details(c_id):
    # channels API endpoint.
    res = youtube.channels().list(id=c_id, 
                                 part='contentDetails').execute()
    return res['items'][0]['contentDetails']['relatedPlaylists']['uploads']                           
    
def video_details(channel_id, query_counts):
    videos = []
    next_page_token = None

    while 1:
        # playlistItems API endpoint.   
        res = youtube.playlistItems().list(playlistId=channel_id,
                                                part='snippet',
                                                maxResults=query_counts,
                                                pageToken=next_page_token).execute()               
        videos += res['items']
        next_page_token = res.get('nextPageToken')
            
        if next_page_token is None:
            break
    return videos

def formatted_print(obj):
    text = json.dumps(obj, indent=4, sort_keys=True)
    print(text)
        
def main():
    channel_upload_id = channel_details("UCEdcHmauNQ0gxzpyAR69asQ")
    videos_list = video_details(channel_upload_id, results_count)
    formatted_print(videos_list)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Completed in {end_time - start_time} seconds')

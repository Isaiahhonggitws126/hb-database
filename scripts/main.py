from calendar import c
from random import sample
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

# Get API key
API_KEY = os.getenv("API_KEY")
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Number of results from a single API call
results_count = 50

# Reading sample csv to fetch youtube queries
sample_queries = pd.read_csv("../data/sample-titles.csv")

channel_id_dict = {
    'channelId': [],
    'channelTitle': [],
}

def get_channel_id(df):
     for queries in range(len(df)):
        time.sleep(1)
        try:
            # Search Endpoint
            search_response = youtube.search().list(part='snippet',
                                        maxResults=2,
                                        q=df.loc[queries]).execute()

            channel_id_dict['channelId'].append(search_response['items'][0]['snippet']['channelId'])
            channel_id_dict['channelTitle'].append(search_response['items'][0]['snippet']['channelTitle'])

        except:
            print("Something went wrong.")


def channel_details(c_id):
    # channels API endpoint.
    channel_response = youtube.channels().list(id=c_id, 
                                 part='contentDetails').execute()
    return channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']                           
    
def video_details(channel_id, query_counts):
    videos = []
    next_page_token = None

    while 1:
        # playlistItems API endpoint.   
        video_response = youtube.playlistItems().list(playlistId=channel_id,
                                                part='snippet',
                                                maxResults=query_counts,
                                                pageToken=next_page_token).execute()               
        videos += video_response['items']
        next_page_token = video_response.get('nextPageToken')
            
        if next_page_token is None:
            break
    return videos

def formatted_print(obj):
    text = json.dumps(obj, indent=4, sort_keys=True)
    print(text)
        
def main():
    # channel_upload_id = channel_details("UCEdcHmauNQ0gxzpyAR69asQ")
    # videos_list = video_details(channel_upload_id, results_count)
    # formatted_print(videos_list)
    get_channel_id(sample_queries)
    print(channel_id_dict)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Completed in {end_time - start_time} seconds')

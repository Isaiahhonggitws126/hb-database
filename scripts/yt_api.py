from dotenv import load_dotenv
import os
import time
from pathlib import Path
from tqdm import tqdm
import json
from googleapiclient.discovery import build

# environment variable
load_dotenv(Path("../.env")) 

# Get API key
API_KEY = os.getenv("API_KEY")
youtube = build('youtube', 'v3', developerKey=API_KEY)

channel_id_dict = {
    'channelId': [],
    'channelTitle': [],
}

def get_channel_id(df):
     for queries in tqdm(range(len(df))):
        time.sleep(1)
        try:
            # Search API endpoint.
            search_response = youtube.search().list(part='snippet',
                                        maxResults=2,
                                        q=df.loc[queries]).execute()

            channel_id_dict['channelId'].append(search_response['items'][0]['snippet']['channelId'])
            channel_id_dict['channelTitle'].append(search_response['items'][0]['snippet']['channelTitle'])

        except:
            print("Something went wrong.")
    

def channel_details(c_id):
    # Channels API endpoint.
    channel_response = youtube.channels().list(id=c_id, 
                                 part='contentDetails').execute()
    return channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']                           
    
def video_details(channel_id):
    videos = []
    next_page_token = None

    while 1:
        # playlistItems API endpoint.   
        video_response = youtube.playlistItems().list(playlistId=channel_id,
                                                part='snippet',
                                                maxResults=50,
                                                pageToken=next_page_token).execute()               
        videos += video_response['items']
        next_page_token = video_response.get('nextPageToken')
            
        if next_page_token is None:
            break
    return videos

def formatted_print(obj):
    json_object = json.dumps(obj, indent=4, sort_keys=True)
    with open('json-data/json-response.json', 'a') as file:
        file.write(json_object)
    
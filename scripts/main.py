import pandas as pd
import time
from dotenv import load_dotenv
from pathlib import Path
import os

# imports from other scripts
from yt_api import get_channel_id, channel_details, video_details, formatted_print, channel_id_dict
from db import connect_to_db, df_to_db, update_db

# environment variable
load_dotenv(Path("../.env"))

# Reading sample csv to fetch youtube queries
sample_queries = pd.read_csv("../data/sample-titles.csv")

def extract_api_data():
    get_channel_id(sample_queries)
    for id in channel_id_dict['channelId']:
        time.sleep(2)
        channel_upload_id = channel_details(id)
        videos_list = video_details(channel_upload_id)
        formatted_print(videos_list)
    return

def load():
    api_response = pd.read_json("json-data/json-response.json")

    # Fetching YT metadata.
    api_data = api_response['snippet']
    youtube_data = pd.json_normalize(api_data)

    youtube_data = youtube_data.rename(columns={
                            'channelId': 'channel_id',
                            'channelTitle': 'channel_title',
                            'playlistId': 'playlist_id',
                            'publishedAt': 'published_at',
                            'videoOwnerChannelId': 'video_owner_channel_id',
                            'videoOwnerChannelTitle': 'video_owner_channel_title',
                            'thumbnails.default.url': 'thumbnails_default_url',
                            'thumbnails.high.url': 'thumbnails_high_url',
                            'thumbnails.standard.url': 'thumbnails_standard_url',
                           }) 


    # Fetches the columns we only need for our DB.
    youtube_data = youtube_data[['channel_id', 
                                'channel_title', 
                                'description',
                                'playlist_id',
                                'published_at',
                                'title',
                                'thumbnails_default_url',
                                'thumbnails_high_url',
                                'thumbnails_standard_url'
                                ]]          
    
    # Loading into DB
    conn = connect_to_db()
    curr = conn.cursor()

    new_channel_df = update_db(curr, youtube_data)

    df_to_db(curr, new_channel_df)

    conn.commit()

            
def main():
    print(load())
   

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Completed in {end_time - start_time} seconds')

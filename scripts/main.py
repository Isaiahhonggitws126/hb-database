import pandas as pd
import time
from yt_api import get_channel_id, channel_details, video_details, formatted_print, channel_id_dict

# Reading sample csv to fetch youtube queries
sample_queries = pd.read_csv("../data/sample-titles.csv")

def extract_api_data():
    get_channel_id(sample_queries)
    for id in channel_id_dict['channelId']:
        time.sleep(2)
        channel_upload_id = channel_details(id)
        videos_list = video_details(channel_upload_id)
        formatted_print(videos_list)

def transform_and_load():
    # Reading local JSON Response object.
    api_response = pd.read_json("json-data/json-response.json")

    # Fetching YT metadata.
    api_data = api_response['snippet']
    youtube_data = pd.json_normalize(api_data)

    #Test the output.
    print(youtube_data)
    youtube_data.to_csv('test-data.csv')    

     
def main():
    extract_api_data()
    transform_and_load()

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Completed in {end_time - start_time} seconds')

import pandas as pd
import time
from yt_api import get_channel_id, channel_details, video_details, formatted_print, channel_id_dict

# Reading sample csv to fetch youtube queries
sample_queries = pd.read_csv("../data/sample-titles.csv")

def main():
    get_channel_id(sample_queries)
    for id in channel_id_dict['channelId']:
        time.sleep(2)
        channel_upload_id = channel_details(id)
        videos_list = video_details(channel_upload_id)
        formatted_print(videos_list)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Completed in {end_time - start_time} seconds')

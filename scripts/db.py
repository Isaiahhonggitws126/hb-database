import psycopg2 as ps
import os
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import INTEGER, TEXT

load_dotenv(Path("../.env"))

# Database Credentials
host=os.getenv('host')
database=os.getenv('database')
port=os.getenv('port')
user=os.getenv('user')
password=os.getenv('password')

def connect_to_db():

    conn = None
    
    try:
       conn = ps.connect(
           host=host,
           database=database,
           user=user,
           password=password,
           port=port           
       )
    except ps.OperationalError as e:
        print(f'Had problem connecting with {e}')

    print("Connected!")
    return conn

def create_table(curr):
    create_table_command = ("""CREATE TABLE IF NOT EXISTS channels(
        channel_id VARCHAR(256) PRIMARY KEY,
        channel_title TEXT NOT NULL,
        description TEXT NOT NULL,
        playlist_id VARCHAR(256),
        published_at DATE NOT NULL,
        title TEXT NOT NULL,
        thumbnails_default_url VARCHAR(2048),
        thumbnails_high_url VARCHAR(2048),
        thumbnails_standard_url varchar(2048)
    )""")
    
    curr.execute(create_table_command)
    print("Table Created!")


def check_if_video_exists(curr, channel_id):
    query = ("""SELECT channel_id FROM channels WHERE channel_id = %s""")
    curr.execute(query, (channel_id,))
    
    return curr.fetchone() is not None


def update_row(curr, channel_id, channel_title, description, playlist_id, published_at, title, thumbnails_default_url, thumbnails_high_url, thumbnails_standard_url):

    query = ("""UPDATE channels
                SET channel_id = %s,
                channel_title = %s,
                description = %s,
                playlist_id = %s,
                published_at = %s,
                title = %s,
                thumbnails_default_url = %s,
                thumbnails_high_url = %s,
                thumbnails_standard_url = %s 
                """)
    cols_to_update = (channel_id, channel_title, description, playlist_id, published_at, title, thumbnails_default_url, thumbnails_high_url, thumbnails_standard_url)
    curr.execute(query, cols_to_update)

def insert_into_table(curr, channel_id, channel_title, description, playlist_id, published_at, title, thumbnails_default_url, thumbnails_high_url, thumbnails_standard_url):
    insert_into_channels = ("""INSERT INTO channels (channel_id, 
                                                    channel_title, 
                                                    description, 
                                                    playlist_id, 
                                                    published_at, 
                                                    title, 
                                                    thumbnails_default_url, 
                                                    thumbnails_high_url, 
                                                    thumbnails_standard_url)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                            """)
    fields_to_update = (channel_id, channel_title, description, playlist_id, published_at, title, thumbnails_default_url, thumbnails_high_url, thumbnails_standard_url)            
    curr.execute(insert_into_channels, fields_to_update)

def truncate_table(curr):
    truncate_table = ("""TRUNCATE TABLE channels""")
    curr.execute(truncate_table)

def df_to_db(curr, df):
    for i, row in df.iterrows():
        insert_into_table(curr, 
                          row['channel_id'],
                          row['channel_title'],
                          row['description'],
                          row['playlist_id'],
                          row['published_at'],
                          row['title'],
                          row['thumbnails_default_url'],
                          row['thumbnails_high_url'],
                          row['thumbnails_standard_url'])

def update_db(curr, df):
    tmp_df = pd.DataFrame(columns=['channel_id', 
                                   'channel_title', 
                                   'description', 
                                   'playlist_id', 
                                   'published_at', 
                                   'title', 
                                   'thumbnails_default_url', 
                                   'thumbnails_high_url', 
                                   'thumbnails_standard_url'])

    for i, row in df.iterrows():
        if check_if_video_exists(curr, row['channel_id']):
            update_row(curr, 
                        row['channel_id'],
                        row['channel_title'],
                        row['description'],
                        row['playlist_id'],
                        row['published_at'],
                        row['title'],
                        row['thumbnails_default_url'],
                        row['thumbnails_high_url'],
                        row['thumbnails_standard_url'])

        else:
            tmp_df = tmp_df.append(row)
        return tmp_df
            
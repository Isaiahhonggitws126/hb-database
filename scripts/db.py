import psycopg2 as ps
import os
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

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


class AppDatabase:
    client = MongoClient(os.getenv("DATABASE_URL"))
    # client = MongoClient(os.environ["DATABASE_URL"])
    db = client["lyriq"]
    user_collection = db["users"]
    artist_collection = db['artists']
    album_collection = db['albums']
    track_collection = db['tracks']


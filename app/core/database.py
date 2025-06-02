from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo.collection import Collection

load_dotenv()


class AppDatabase:
    client = MongoClient(os.getenv("DATABASE_URL"))
    # client = MongoClient(os.environ["DATABASE_URL"])
    db = client["lyriq"]
    user_collection = db["users"]
    artist_collection = db['artists']
    album_collection = db['albums']
    track_collection = db['tracks']


_db = AppDatabase()


def get_artist_collection() -> Collection:
    return _db.artist_collection


def get_album_collection() -> Collection:
    return _db.album_collection


def get_track_collection() -> Collection:
    return _db.track_collection

def get_user_collection() -> Collection:
    return _db.user_collection
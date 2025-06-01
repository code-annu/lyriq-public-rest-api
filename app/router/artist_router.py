from bson.errors import InvalidId
from starlette import status

from app.core.exceptions import NotFoundException
from app.service.artist_service import ArtistService
from app.core.database import AppDatabase
from fastapi import APIRouter, HTTPException

_db = AppDatabase()
artist_router = APIRouter()
_artist_service = ArtistService(_db.artist_collection)


@artist_router.get("/get/{artist_id}")
def get_artist(artist_id: str):
    try:
        return _artist_service.read(artist_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid artist id format")
    except NotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with ID {artist_id} not found")


@artist_router.get("/shuffle")
def list_shuffled_artist(limit: int):
    return _artist_service.shuffled_data(size=limit)


@artist_router.post("/multiple")
def get_multiple_artists(artist_ids: list[str]):
    try:
        return _artist_service.read_many(artist_ids)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid artist id format")


@artist_router.get("/search")
def search_artist(query: str):
    return _artist_service.search_artist(query)

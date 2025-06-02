from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException
from starlette import status

from app.core.exceptions import NotFoundException
from app.service.track_service import TrackService

track_router = APIRouter()
_track_service = TrackService()


@track_router.get("/get/{track_id}")
def get_track(track_id: str):
    try:
        return _track_service.get_track(track_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid album id format")
    except NotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album with ID {track_id} not found")


@track_router.get('/shuffle')
def list_shuffle_tracks(limit: int):
    return _track_service.list_shuffled_tracks(limit)


@track_router.get('/search')
def search_track(query: str):
    return _track_service.search_track(query)

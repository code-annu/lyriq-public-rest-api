from bson.errors import InvalidId
from starlette import status

from app.core.exceptions import NotFoundException
from app.core.security import get_current_user
from app.model.user_model import User
from app.service.artist_service import ArtistService
from fastapi import APIRouter, HTTPException, Depends

artist_router = APIRouter()
_artist_service = ArtistService()


@artist_router.get("/get/{artist_id}")
def get_artist(artist_id: str,user:User=Depends(get_current_user)):
    try:
        return _artist_service.get_artist(artist_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid artist id format")
    except NotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with ID {artist_id} not found")


@artist_router.get("/shuffle")
def list_shuffled_artist(limit: int,user:User=Depends(get_current_user)):
    return _artist_service.list_shuffled_artist(limit=limit)


@artist_router.post("/multiple")
def get_multiple_artists(artist_ids: list[str],user:User=Depends(get_current_user)):
    try:
        return _artist_service.get_many_artist(artist_ids)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid artist id format")


@artist_router.get("/search")
def search_artist(query: str,user:User=Depends(get_current_user)):
    return _artist_service.search_artist(query)

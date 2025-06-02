from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException
from starlette import status

from app.core.exceptions import NotFoundException
from app.service.album_service import AlbumService

album_router = APIRouter()
_album_service = AlbumService()


@album_router.get("/get/{album_id}")
def get_album(album_id: str):
    try:
        return _album_service.get_album(album_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid album id format")
    except NotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album with ID {album_id} not found")


@album_router.get('/shuffle')
def list_shuffle_albums(limit: int):
    return _album_service.list_shuffled_album(limit)


@album_router.get('/search')
def search_album(query: str):
    return _album_service.search_album(query)

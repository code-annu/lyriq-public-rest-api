from fastapi import Depends

from .base_service import BaseService
from app.model.album_model import *
from pymongo.collection import Collection
from app.repository.artist_repository import ArtistRepository
from app.core.database import *


class AlbumService(BaseService[Album]):
    def __init__(self):
        super().__init__(collection=Depends(get_album_collection), model=Album)

    def search_album(self, query: str) -> list[Album]:
        return super().search_data(index_name="albumNameIndex", path_name="name", query=query)

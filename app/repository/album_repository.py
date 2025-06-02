from app.model.album_model import *
from pymongo.collection import Collection

from app.repository.base_repository import BaseRepository


class AlbumRepository(BaseRepository[Album]):
    def __init__(self, collection: Collection):
        super().__init__(collection, Album)

    def search_album(self, query: str) -> list[Album]:
        return super().search_data(index_name="albumNameIndex", path_name="name", query=query)

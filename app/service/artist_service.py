from .base_service import BaseService
from app.model.artist_model import *
from pymongo.collection import Collection


class ArtistService(BaseService[Artist]):
    def __init__(self, collection: Collection):
        super().__init__(collection, Artist)

    def search_artist(self, query: str) -> list[Artist]:
        return super().search_data(index_name="artistNameIndex", path_name="name", query=query)

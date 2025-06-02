from app.core.database import get_artist_collection
from app.model.artist_model import *
from app.repository.base_repository import BaseRepository


class ArtistRepository(BaseRepository[Artist]):
    def __init__(self):
        super().__init__(get_artist_collection(), Artist)

    def get_artist(self, artist_id: str) -> Artist:
        return super().read(artist_id)

    def get_many_artists(self, artist_ids: list[str]) -> list[Artist]:
        return super().read_many(artist_ids)

    def list_shuffled_artist(self, limit: int) -> list[Artist]:
        return super().shuffled_data(size=limit)

    def search_artist(self, query: str) -> list[Artist]:
        return super().search_data(index_name="artistNameIndex", path_name="name", query=query)

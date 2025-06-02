from app.core.database import get_album_collection
from app.model.album_model import *
from app.repository.base_repository import BaseRepository


class AlbumRepository(BaseRepository[Album]):
    def __init__(self):
        super().__init__(get_album_collection(), Album)

    def get_album(self, album_id: str) -> Album:
        return super().read(album_id)

    def get_many_albums(self, album_ids: list[str]) -> list[Album]:
        return super().read_many(album_ids)

    def list_shuffled_album(self, limit: int) -> list[Album]:
        return super().shuffled_data(size=limit)

    def search_album(self, query: str) -> list[Album]:
        return super().search_data(index_name="albumIndexName", path_name="title", query=query)

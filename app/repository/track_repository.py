from app.repository.base_repository import BaseRepository
from app.core.database import get_track_collection
from app.model.track_model import *


class TrackRepository(BaseRepository[Track]):
    def __init__(self):
        super().__init__(get_track_collection(), Track)

    def get_track(self, track_id: str) -> Track:
        return super().read(track_id)

    def get_many_tracks(self, track_ids: list[str]) -> list[Track]:
        return super().read_many(track_ids)

    def list_shuffled_track(self, limit: int) -> list[Track]:
        return super().shuffled_data(size=limit)

    def search_track(self, query: str) -> list[Track]:
        return super().search_data(index_name="trackIndexName", path_name="title", query=query)

from app.repository.artist_repository import ArtistRepository


class ArtistService:
    _artist_repository = ArtistRepository()

    def get_artist(self, artist_id):
        return self._artist_repository.get_artist(artist_id)

    def get_many_artist(self, artist_ids):
        return self._artist_repository.get_many_artists(artist_ids)

    def search_artist(self, query: str):
        return self._artist_repository.search_artist(query)

    def list_shuffled_artist(self, limit: int):
        return self._artist_repository.shuffled_data(size=limit)

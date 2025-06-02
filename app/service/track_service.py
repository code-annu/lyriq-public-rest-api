from app.repository.album_repository import AlbumRepository
from app.repository.artist_repository import ArtistRepository
from app.repository.track_repository import TrackRepository
from app.model.track_model import *


class TrackService:
    _album_repository = AlbumRepository()
    _artist_repository = ArtistRepository()
    _track_repository = TrackRepository()

    def _prepare_track_response(self, track: Track):
        album = self._album_repository.get_album(track.album_id)
        track_album = TrackAlbum(id=album.id, title=album.title, cover_url=album.cover_url)

        artists = self._artist_repository.get_many_artists(track.artist_ids)
        track_artists: list[TrackArtist] = []
        for artist in artists:
            track_artists.append(TrackArtist(id=artist.id, name=artist.name, img_url=artist.img_url))

        return TrackResponse(
            id=track.id,
            title=track.title,
            release_date=track.release_date,
            cover_url=track.cover_url,
            audio_url=track.audio_url,
            duration=track.duration,
            album=track_album,
            artists=track_artists
        )

    def get_track(self, track_id) -> TrackResponse:
        track = self._track_repository.get_track(track_id)
        return self._prepare_track_response(track)

    def list_shuffled_tracks(self, limit: int) -> list[TrackResponse]:
        shuffled_tracks = self._track_repository.list_shuffled_track(limit)
        track_response_list: list[TrackResponse] = []
        for track in shuffled_tracks:
            track_response_list.append(self._prepare_track_response(track))
        return track_response_list

    def search_track(self, query: str) -> list[TrackResponse]:
        found_tracks = self._track_repository.search_track(query)
        track_response_list: list[TrackResponse] = []
        for track in found_tracks:
            track_response_list.append(self._prepare_track_response(track))
        return track_response_list

from app.repository.album_repository import AlbumRepository
from app.repository.artist_repository import ArtistRepository
from app.repository.track_repository import TrackRepository
from app.model.album_model import *


class AlbumService:
    _album_repository = AlbumRepository()
    _artist_repository = ArtistRepository()
    _track_repository = TrackRepository()

    def _prepare_album_response(self, album: Album):
        artists = self._artist_repository.get_many_artists(album.artist_ids)
        album_artists: list[AlbumArtist] = []
        for artist in artists:
            album_artists.append(AlbumArtist(id=artist.id, name=artist.name, img_url=artist.img_url))

        tracks = self._track_repository.get_many_tracks(album.track_ids)
        album_tracks: list[AlbumTrack] = []
        for track in tracks:
            album_tracks.append(
                AlbumTrack(id=track.id, title=track.title, cover_url=track.cover_url, audio_url=track.audio_url))

        return AlbumResponse(
            id=album.id,
            title=album.title,
            release_date=album.release_date,
            total_tracks=album.total_tracks,
            cover_url=album.cover_url,
            artists=album_artists,
            tracks=album_tracks
        )

    def get_album(self, album_id) -> AlbumResponse:
        album = self._album_repository.get_album(album_id)
        return self._prepare_album_response(album)

    def list_shuffled_album(self, limit: int) -> list[AlbumResponse]:
        shuffled_albums = self._album_repository.list_shuffled_album(limit)
        album_response_list: list[AlbumResponse] = []
        for album in shuffled_albums:
            album_response_list.append(self._prepare_album_response(album))
        return album_response_list

    def search_album(self, query: str) -> list[AlbumResponse]:
        found_albums = self._album_repository.search_album(query)
        album_response_list: list[AlbumResponse] = []
        for album in found_albums:
            album_response_list.append(self._prepare_album_response(album))
        return album_response_list

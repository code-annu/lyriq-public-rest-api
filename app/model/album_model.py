from pydantic import BaseModel


class _AlbumBase(BaseModel):
    id: str
    title: str
    release_date: str
    total_tracks: int
    cover_url: str


class Album(_AlbumBase):
    artist_ids: list[str]
    track_ids: list[str]


class AlbumArtist(BaseModel):
    id: str
    name: str
    img_url: str


class AlbumTrack(BaseModel):
    id: str
    title: str
    cover_url: str
    audio_url: str


class AlbumResponse(_AlbumBase):
    artists: list[AlbumArtist]
    tracks: list[AlbumTrack]

from pydantic import BaseModel


class _TrackBase(BaseModel):
    id: str
    title: str
    release_date: str
    cover_url: str
    audio_url: str
    duration: float
    lyrics: str | None = None


class Track(_TrackBase):
    artist_ids: list[str]
    album_id: str


class TrackAlbum(BaseModel):
    id: str
    title: str
    cover_url: str


class TrackArtist(BaseModel):
    id: str
    name: str
    img_url: str


class TrackResponse(_TrackBase):
    pass
    album: TrackAlbum
    artists: list[TrackArtist]

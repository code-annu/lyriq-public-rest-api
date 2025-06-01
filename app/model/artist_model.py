from pydantic import BaseModel


class Artist(BaseModel):
    id: str
    name: str
    birth_year: int
    gender: str
    img_url: str

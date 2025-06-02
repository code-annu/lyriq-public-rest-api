from fastapi import FastAPI
from app.router.artist_router import artist_router
from app.router.album_router import album_router

app = FastAPI()

BASE_API_URL = '/public/api/v1'

app.include_router(router=artist_router, prefix=BASE_API_URL + '/artist')
app.include_router(router=album_router, prefix=BASE_API_URL + '/album')

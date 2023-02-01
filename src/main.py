from fastapi import FastAPI
from routers import s3
from routers import OAuth2

app = FastAPI()
app.include_router(s3.router)
app.include_router(OAuth2.router)
from fastapi import FastAPI
from conf import tags_metadata

app = FastAPI(title= 'game', openapi_tags=tags_metadata)

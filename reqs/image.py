from .app import app

from fastapi.responses import FileResponse

@app.get("/image/octopus_fon", tags=["images"])
async def image_octopus_fon():
    return FileResponse("static/img/octopus_fon.png")

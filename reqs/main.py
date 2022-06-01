from .app import app
from fastapi.responses import RedirectResponse

@app.get("/")
async def main():
    return RedirectResponse('/login')

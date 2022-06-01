from .app import app
from typing import Optional
from fastapi import Header, Body
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from clas import User 
templates = Jinja2Templates(directory="static/templates")
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get("/login", tags=["users"],)
async def login(request: Request):
    "Возвращаем страницу для логина"
    return templates.TemplateResponse("login.html", {"request": request})    

@app.post("/login", tags=["users"])
async def login(request: Request):
    form = await request.form()
    USERNAME = form.get('username')
    PASSWORD = form.get('password')
    if USERNAME == '' or PASSWORD == '':
        return templates.TemplateResponse("login.html", {"request": request, "message" : "test"})    

    return templates.TemplateResponse("login.html", {"message": User.loging(USERNAME,PASSWORD)})    



@app.put("/update_password", tags=["users"])
async def update_password(
        token: Optional[str] = Header(None),
        password: Optional[str] = Body(None)
        ):
    "Изменение пароля пользователя"
    if token is None or password is None:
        return None
    else:
        return await User.update_password(token,password)


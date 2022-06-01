from uuid import uuid4, UUID
from pydantic import BaseModel, Field

from base import database, t_users
from conf import hash_password

class User(BaseModel):
    u_id: UUID = Field(default_factory=uuid4)
    gamename: str
    username: str
    password_hash: str
    admin: bool

    async def add(GAMENAME,USERNAME,PASSWORD):
        "Добавление пользователя"
        query = t_users.select(t_users.c.username == USERNAME)
        res = await database.fetch_one(query)
        if not res is None:
            return {"error" : f"Пользователь {username} уже существует" }

        else:
            values = { "u_id" : uuid4(),
                       "username" : USERNAME,
                       "password_hash" : hash_password(PASSWORD),
                       "admin" : False
                    }
            query = t_users.insert().values(**values)
            await database.execute(query)
            return {"message" : "Пользователь добавлен"}

    async def loging(USERNAME,PASSWORD):
        "Вход в систему, получение токена"
        query = t_users.select(t_users.c.username == USERNAME)

        res = await database.fetch_one(query)
        if res is None:
            return {"error" : f"Пользователя {USERNAME} не существует"}
        else:
            if not res["password_hash"] == hash_password(PASSWORD):
                return {"error" : "Неправильный пароль!"}
            else:
                TOKEN = uuid4()
                query = t_users.update() \
                        .where(t_users.c.username == USERNAME) \
                        .values(token = TOKEN)
                await database.execute(query)

                return {"message"  : "Вы успешно вошли в систему",
                        "gamename" : res["gamename"],
                        "username" : res["username"],
                        "token"    : TOKEN }
    
    async def cheak_token(TOKEN):
        "Проверка токена пользователя"
        query = t_users.select(t_users.c.token == TOKEN)

        res = await database.fetch_one(query)

        if res is None:
            return {"error" : "Токен недействителен"}
        else:
            return True

    async def update_password(TOKEN,PASSWORD):
        "Замена старого пароля на новый"
        query = t_users.select(t_users.c.token == TOKEN)

        res = await database.fetch_one(query)

        if res is None:
            return {"error" : "Нет такого пользователя!"}
        else:
            query = t_users.update() \
                    .where(t_users.c.token == TOKEN) \
                    .values(password_hash = hash_password(PASSWORD))
            
            await database.execute(query)
            return {"message" : "Пароль изменён"}



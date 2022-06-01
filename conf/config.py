from starlette.config import Config
from passlib.hash import md5_crypt

config = Config(".conf")

DATABASE_URL = config("DATABASE_URL",cast=str)
SALT = config("SALT", cast=str)


def hash_password(password: str) -> str:
    "Хеширование пароля"
    return md5_crypt.encrypt(password,salt=SALT)

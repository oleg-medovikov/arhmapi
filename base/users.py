from .base import metadata

from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

t_users = Table(
    "users",
    metadata,
    Column('u_id', UUID(), primary_key=True, default=uuid.uuid4), #уникальный идентификатор пользователя
    Column('gamename', String), # Имя внутри игры
    Column('username', String), #логин пользователя
    Column('password_hash', String), # хеш пароля
    Column('admin', Boolean), # является ли админом
    Column('token', UUID()), # токен пользователя, на будущее 
        )

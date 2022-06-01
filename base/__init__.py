from .base import database, metadata, engine
from .users import t_users

metadata.create_all(engine)

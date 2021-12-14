from fastapi_users.authentication import JWTAuthentication
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from .models import User
from .schemas import UserDB
from core.db import SessionLocal

users = User.__table__
user_db = SQLAlchemyUserDatabase(UserDB, SessionLocal, users)

SECRET = 'asjajasoidauj29hsd87sd7hh878d9shd9'

auth_backends = [
    JWTAuthentication(secret=SECRET, lifetime_seconds=3600)
]



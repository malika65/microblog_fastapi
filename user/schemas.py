import uuid
from typing import Optional

import pydantic
from fastapi_users import models
from pydantic import EmailStr, BaseModel


class User(models.BaseUser):
    pass



class UserCreate(User, models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
import databases
from sqlalchemy.orm import Session

from .models import posts
from .schemas import PostCreate
from core.db import database

async def get_post_list():
    return await database.fetch_all(query=posts.select())


async def create_post(item: PostCreate):
    post = posts.insert().values(**item.dict())
    return await database.execute(post)
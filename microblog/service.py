import databases
from sqlalchemy.orm import Session
from sqlalchemy import select

from .models import posts, Post
from .schemas import PostCreate
from core.db import database

async def get_post_list():
    return await database.fetch_all(query=posts.select())

async def get_post(pk: int):
    # return await database.fetch_one(query=select([posts]).where(Post.id==pk))
    return await database.fetch_one(query=posts.select().where(Post.id==pk))


async def create_post(item: PostCreate):
    post = posts.insert().values(**item.dict())
    return await database.execute(post)
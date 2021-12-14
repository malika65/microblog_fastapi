from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from core.utils import get_db
from .schemas import PostCreate, PostList, PostSingle
from . import service


router = APIRouter()

@router.get('/', response_model=List[PostList])
async def post_list():
    return await service.get_post_list()

@router.post('/')
async def post_create(item: PostCreate):
    return await service.create_post(item)

@router.get('/{pk}', response_model=PostSingle)
async def post_single(pk: int):
    return await service.get_post(pk)
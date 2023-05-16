from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.base import get_db
from db.base import SessionLocal
from repository.user import get_all, get_by_id, get_by_email, create, update, delete
from models.user import User, UserIn
from .depends import get_current_user

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(
        db: Session = Depends(get_db),
        limit: int = 100,
        skip: int = 0):
    return await get_all(db=db, limit=limit, skip=skip)


@router.post("/", response_model=User)
async def create_user(
        user: UserIn,
        db: Session = Depends(get_db)):

    return await create(db=db, u=user)


@router.put("/", response_model=User)
async def update_user(
        user_id: int,
        user: UserIn,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    old_user = await get_by_id(db=db, user_id=user_id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return await update(db=db, user_id=user_id, u=user)


@router.delete("/{user_id}")
async def delete_user(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    return await delete(db=db, user_id=user_id)
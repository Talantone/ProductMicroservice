from typing import List, Optional

import sqlalchemy

from db.users import User
import models.user
from sqlalchemy.orm import Session
from core.security import hash_password


async def get_all(db: Session, limit: int = 100, skip: int = 0):
    return db.query(User).offset(skip).limit(limit).all()


async def get_by_id(db: Session, user_id: int) -> Optional[models.user.User]:
    return db.query(User).filter(User.id == user_id).first()


async def create(db: Session, u: models.user.UserIn) -> models.user.User:
    user = User(
        email=u.email,
        hashed_password=hash_password(u.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def update(db: Session, user_id: int, u: models.user.UserUpdate) -> models.user.User:
    user = models.user.User(
        id=user_id,
        email=u.email,
        hashed_password=hash_password(u.password),

    )
    values = {**user.dict()}
    values.pop("id", None)
    db.execute(sqlalchemy.update(User).where(User.id == user_id).values(**values))

    return user


async def get_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

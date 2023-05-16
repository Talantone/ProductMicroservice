from typing import Any

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from repository.user import get_by_email

from db.base import get_db
from core.security import JWTBearer, decode_access_token


async def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(JWTBearer()),
) -> HTTPException | Any:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await get_by_email(db=db, email=email)
    if user is None:
        return cred_exception
    return user

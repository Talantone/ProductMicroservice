from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.security import verify_password, create_access_token
#from endpoints.depends import get_user_repository
from models.token import Token, Login
from repository.user import get_by_email
from db.base import get_db
router = APIRouter()


@router.post("/", response_model=Token)
async def login(
        login: Login,
        db: Session = Depends(get_db)
):
    user = await get_by_email(db=db, email=login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    return Token(
        access_string=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )

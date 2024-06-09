from fastapi import APIRouter, Depends, Query, HTTPException, status

from src.accessors.user_accessor import fetch_user, create_user, fetch_user_by_email
from src.models.schemas import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/", response_model=User)
async def create_new_user(user: UserCreate):
    user = create_user(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    return user


@router.get("/", response_model=User)
async def fetch_user(email_id: str = Query(...)):
    user = fetch_user_by_email(email_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


from src.models.schemas import User, UserCreate
from src.modules.fake_db import users

FAKER_USERS = users


def create_user(user: UserCreate):
    increment_id = len(FAKER_USERS) + 1
    db_user = User(id=increment_id, **user.dict())
    FAKER_USERS[increment_id] = db_user
    return FAKER_USERS[increment_id]


def fetch_user(user_id: int):

    if user_id in FAKER_USERS:
        return FAKER_USERS[user_id]
    else:
        return None


def fetch_user_by_email(email_id: str):

    for user in FAKER_USERS.values():
        if user.email_id == email_id:
            return user

    return None


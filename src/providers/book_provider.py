from src.accessors.user_accessor import fetch_user
from src.models.schemas import CollectionDTO, UserDTO
from src.modules.fake_db import users, collections, books

FAKER_USERS = users
FAKER_COLLECTIONS = collections
FAKER_BOOKS = books


def fetch_all_collections(user_id: int):
    user = FAKER_USERS[user_id]
    user_collections = [collection for collection in FAKER_COLLECTIONS.values() if collection.user_id == user_id]
    return UserDTO(collections=[CollectionDTO(books=fetch_all_books(collection_id=collection.id), **collection.dict()) for collection in user_collections], **user.dict())


def fetch_all_books(collection_id: int):
    collection_books = [book for book in FAKER_BOOKS.values() if book.collection_id == collection_id]
    return collection_books

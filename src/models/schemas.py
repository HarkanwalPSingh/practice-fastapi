from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email_id: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class CollectionBase(BaseModel):
    name: str
    user_id: int


class CollectionCreate(CollectionBase):
    pass


class Collection(CollectionBase):
    id: int

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    name: str
    author: str
    collection_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


class CollectionDTO(Collection):
    books: List[Book]


class UserDTO(User):
    collections: List[CollectionDTO]

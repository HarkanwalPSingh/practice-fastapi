from src.models.schemas import CollectionCreate, Collection
from src.modules.fake_db import collections, users

FAKER_COLLECTIONS = collections
FAKER_USERS = users


# TODO: Add exception mapping
def create_collection(collection: CollectionCreate):
    if collection.user_id not in FAKER_USERS:
        return None
    collection_id = len(FAKER_COLLECTIONS) + 1
    db_collection = Collection(id=collection_id, user_id=collection.user_id, name=collection.name)
    FAKER_COLLECTIONS[collection_id] = db_collection
    return FAKER_COLLECTIONS[collection_id]

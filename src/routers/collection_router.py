from fastapi import APIRouter, HTTPException, status, Query

from src.accessors.collection_accessor import create_collection
from src.models.schemas import Collection, CollectionCreate, CollectionDTO, UserDTO
from src.providers.book_provider import fetch_all_collections

router = APIRouter(
    prefix="/collections",
    tags=["collections"]
)


@router.post("/", response_model=Collection)
async def create_new_collection(collection: CollectionCreate):
    new_collection = create_collection(collection)
    if not new_collection:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user id")
    return new_collection


@router.get("/all", response_model=UserDTO)
async def fetch_all_user_collections(user_id: int = Query(...)):
    all_collections = fetch_all_collections(user_id)
    if not all_collections:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No collection found for user id {user_id}")
    return all_collections

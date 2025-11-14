from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.item import Item, ItemCreate
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=Item)
def create_item(item_in: ItemCreate, db = Depends(get_db)):
    item_dict = item_in.dict()
    new_item = db.add_item(item_dict)
    return Item(**new_item)

@router.get("/", response_model=List[Item])
def list_items(db = Depends(get_db)):
    return [Item(**item) for item in db.list_items()]

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int, db = Depends(get_db)):
    item = db.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**item)
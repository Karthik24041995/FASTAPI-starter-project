from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.user import User, UserCreate
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=User)
def create_user(user_in: UserCreate, db = Depends(get_db)):
    user_dict = user_in.dict()
    new_user = db.add_user(user_dict)
    return User(**new_user)

@router.get("/", response_model=List[User])
def list_users(db = Depends(get_db)):
    return [User(**user) for user in db.list_users()]

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db = Depends(get_db)):
    user = db.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user)
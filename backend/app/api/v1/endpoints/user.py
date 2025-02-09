from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.schemas.user import UserCreate, UserResponse
from app.db.database import get_db
from app.crud.user import UserCRUD


router = APIRouter(tags=["users"])


@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = await UserCRUD.get_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await UserCRUD.create(db, user)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await UserCRUD.get_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = await UserCRUD.delete(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted Successfully!"}

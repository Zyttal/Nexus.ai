from typing import Optional
from sqlalchemy.orm import Session

from app.db.schemas.user import UserCreate
from app.db.models.user import User


class UserCRUD:
    @staticmethod
    async def create(db: Session, user: UserCreate) -> User:
        db_user = User(
            email=user.email, hashed_password=get_password_hash(user.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    async def get_by_id(db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    async def get_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    async def update(db: Session, user_id: int, data: dict) -> Optional[User]:
        db.query(User).filter(User.id == user_id).update(data)
        db.commit()
        return await UserCRUD.get_by_id(db, user_id)

    @staticmethod
    async def delete(db: Session, user_id: int) -> bool:
        user = await UserCRUD.get_by_id(db, user_id)
        if user:
            db.delete(user)
            db.commit()
            return True
        return False

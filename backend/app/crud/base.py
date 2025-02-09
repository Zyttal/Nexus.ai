from typing import Generic, Type, TypeVar
from sqlalchemy.orm import Session
from app.db.database import Base


ModelType = TypeVar("ModelType", bound=Base)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model: type[ModelType] = model

    async def get(self, db: Session, id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == id).first()

    async def create(self, db: Session, data: dict) -> ModelType:
        db_obj = self.model(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def update(self, db: Session, data: dict) -> ModelType:
        db_obj = db.query(self.model).filter(self.model.id == id).first()

        if not db_obj:
            return None

        for key, value in data.items():
            setattr(db_obj, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

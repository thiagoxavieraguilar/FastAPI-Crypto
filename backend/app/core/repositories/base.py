from typing import Any, Generic, List, Optional, Type, TypeVar

import sqlalchemy
from sqlalchemy.orm import Query, Session

from app.core.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get(self, id: Any) -> ModelType:
        obj: ModelType = self.db.query(self.model).filter_by(id=id).one()
        return obj

    def query(self) -> Query:
        return self.db.query(self.model)

    def list(self) -> List[ModelType]:
        objs: List[ModelType] = self.db.query(self.model).all()
        return objs

    def create(self, db_obj: ModelType) -> ModelType:
        self.db.add(db_obj)
        try:
            self.save()
        except sqlalchemy.exc.IntegrityError as e:
            self.db.rollback()
            raise e
        self.refresh(db_obj)
        return db_obj

    def update(self, db_obj: ModelType) -> Optional[ModelType]:
        self.db.add(db_obj)
        self.save()
        return db_obj

    def delete(self, id: Any) -> None:
        db_obj = self.db.query(self.model).get(id)
        self.db.delete(db_obj)
        self.save()

    def refresh(self, db_obj: ModelType):
        self.db.refresh(db_obj)

    def save(self):
        self.db.commit()

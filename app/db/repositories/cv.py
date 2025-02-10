from sqlalchemy.orm import Session
from app.db.models.cv import CV
from typing import List, Optional

class CVRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, content: str) -> CV:
        cv = CV(title=title, content=content)
        self.db.add(cv)
        self.db.commit()
        self.db.refresh(cv)
        return cv

    def get_by_id(self, cv_id: int) -> Optional[CV]:
        return self.db.query(CV).filter(CV.id == cv_id).first()

    def get_all(self) -> List[CV]:
        return self.db.query(CV).all()

    def update(self, cv_id: int, title: str = None, content: str = None) -> Optional[CV]:
        cv = self.get_by_id(cv_id)
        if cv:
            if title is not None:
                cv.title = title
            if content is not None:
                cv.content = content
            self.db.commit()
            self.db.refresh(cv)
        return cv

    def delete(self, cv_id: int) -> bool:
        cv = self.get_by_id(cv_id)
        if cv:
            self.db.delete(cv)
            self.db.commit()
            return True
        return False

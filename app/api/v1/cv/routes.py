from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.db.base import get_db
from app.db.repositories.cv import CVRepository

router = APIRouter()

class CVBase(BaseModel):
    title: str
    content: str

class CVCreate(CVBase):
    pass

class CV(CVBase):
    id: int
    class Config:
        from_attributes = True

@router.post("/", response_model=CV)
def create_cv(cv: CVCreate, db: Session = Depends(get_db)):
    cv_repo = CVRepository(db)
    return cv_repo.create(title=cv.title, content=cv.content)

@router.get("/{cv_id}", response_model=CV)
def read_cv(cv_id: int, db: Session = Depends(get_db)):
    cv_repo = CVRepository(db)
    cv = cv_repo.get_by_id(cv_id)
    if cv is None:
        raise HTTPException(status_code=404, detail="CV not found")
    return cv

@router.get("/", response_model=List[CV])
def read_cvs(db: Session = Depends(get_db)):
    cv_repo = CVRepository(db)
    return cv_repo.get_all()

@router.put("/{cv_id}", response_model=CV)
def update_cv(cv_id: int, cv: CVCreate, db: Session = Depends(get_db)):
    cv_repo = CVRepository(db)
    updated_cv = cv_repo.update(cv_id, title=cv.title, content=cv.content)
    if updated_cv is None:
        raise HTTPException(status_code=404, detail="CV not found")
    return updated_cv

@router.delete("/{cv_id}")
def delete_cv(cv_id: int, db: Session = Depends(get_db)):
    cv_repo = CVRepository(db)
    if not cv_repo.delete(cv_id):
        raise HTTPException(status_code=404, detail="CV not found")
    return {"ok": True}

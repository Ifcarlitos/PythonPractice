from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..db import get_db

router = APIRouter(prefix="/courses", tags=["courses"])


@router.post("/", response_model=schemas.CourseRead)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


@router.get("/", response_model=List[schemas.CourseRead])
def list_courses(db: Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return courses


@router.post("/{course_id}/lessons", response_model=schemas.LessonRead)
def create_lesson(
    course_id: int, lesson: schemas.LessonCreate, db: Session = Depends(get_db)
):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_lesson = models.Lesson(course_id=course_id, **lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson


@router.get("/{course_id}/lessons", response_model=List[schemas.LessonRead])
def list_lessons(course_id: int, db: Session = Depends(get_db)):
    lessons = (
        db.query(models.Lesson)
        .filter(models.Lesson.course_id == course_id)
        .order_by(models.Lesson.position)
        .all()
    )
    return lessons

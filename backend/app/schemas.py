from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LessonBase(BaseModel):
    title: str
    content: Optional[str] = None
    position: int = 0


class LessonCreate(LessonBase):
    pass


class LessonRead(LessonBase):
    id: int

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    level: Optional[str] = None


class CourseCreate(CourseBase):
    pass


class CourseRead(CourseBase):
    id: int
    created_at: datetime
    lessons: List[LessonRead] = []

    class Config:
        orm_mode = True

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


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

    model_config = ConfigDict(from_attributes=True)


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

    model_config = ConfigDict(from_attributes=True)

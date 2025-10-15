from pydantic import BaseModel
from typing import List, Optional

# User schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    is_admin: Optional[bool] = False

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_admin: bool
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Student schemas
class CourseBase(BaseModel):
    name: str
    description: Optional[str] = None

class Course(CourseBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    courses: List[Course] = []
    class Config:
        orm_mode = True

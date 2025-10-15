from sqlalchemy.orm import Session
from models import User, Student
from auth import hash_password, verify_password

# User CRUD
def create_user(db: Session, username: str, email: str, password: str, is_admin: bool = False):
    user = User(username=username, email=email, hashed_password=hash_password(password), is_admin=is_admin)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# Student CRUD
def create_student(db: Session, name: str, email: str):
    student = Student(name=name, email=email)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def update_student(db: Session, student_id: int, name: str = None, email: str = None):
    student = get_student(db, student_id)
    if student:
        if name:
            student.name = name
        if email:
            student.email = email
        db.commit()
        db.refresh(student)
    return student

def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    if student:
        db.delete(student)
        db.commit()
    return student

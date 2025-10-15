from sqlalchemy.orm import Session
from models import Student, Course

# Create a new student
def create_student(db: Session, name: str, email: str):
    student = Student(name=name, email=email)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

# Read all students
def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

# Read student by ID
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

# Update student
def update_student(db: Session, student_id: int, name: str = None, email: str = None):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        if name:
            student.name = name
        if email:
            student.email = email
        db.commit()
        db.refresh(student)
    return student

# Delete student
def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student

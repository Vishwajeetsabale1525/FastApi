from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models, schemas, crud, auth
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System with Auth")

# ---------------- User Routes ----------------
@app.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.create_user(db, user.username, user.email, user.password, user.is_admin)

@app.post("/token", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": user.username, "is_admin": user.is_admin})
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: str = Depends(auth.oauth2_scheme), db: Session = Depends(get_db)):
    payload = auth.decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = crud.get_user_by_username(db, payload.get("sub"))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def admin_required(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user

# ---------------- Student Routes ----------------
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, 
                   db: Session = Depends(get_db), 
                   current_user: models.User = Depends(admin_required)):
    return crud.create_student(db, student.name, student.email)

@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, 
                  db: Session = Depends(get_db), 
                  current_user: models.User = Depends(get_current_user)):
    return crud.get_students(db, skip, limit)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db), 
                 current_user: models.User = Depends(get_current_user)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db),
                   current_user: models.User = Depends(admin_required)):
    updated = crud.update_student(db, student_id, name=student.name, email=student.email)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db), 
                   current_user: models.User = Depends(admin_required)):
    deleted = crud.delete_student(db, student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}

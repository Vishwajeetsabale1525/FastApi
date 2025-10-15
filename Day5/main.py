from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database, models, schemas, crud
from middleware import LoggingMiddleware

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Day 5 Middleware, CORS & DI Example")

# Add middleware for logging
app.add_middleware(LoggingMiddleware)

# Configure CORS
origins = [
    "http://localhost:3000",           # Local development frontend
    "https://dashboard.myapp.com",     # Example production frontend
            
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db, item)

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_items(db, skip, limit)

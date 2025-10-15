from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:1111@127.0.0.1:5432/middleware_cors_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()   # <-- single Base used everywhere

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
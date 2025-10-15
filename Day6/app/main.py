from fastapi import FastAPI
from app.routers import auth
from app.db.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Booking API")

# Include routers
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Movie Booking API"}

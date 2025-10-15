# app/main.py
from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="FastAPI Theater Booking")

# Include routers
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to Theater Booking API"}

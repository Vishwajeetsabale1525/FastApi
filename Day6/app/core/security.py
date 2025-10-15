# Simple placeholder for security functions

def hash_password(password: str) -> str:
    # In real app, use bcrypt or passlib
    return password + "_hashed"

def verify_password(plain: str, hashed: str) -> bool:
    return hash_password(plain) == hashed

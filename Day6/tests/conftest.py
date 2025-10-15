import pytest

@pytest.fixture
def sample_user():
    return {"name": "John Doe", "email": "john@example.com", "password": "123456"}

import pytest

@pytest.fixture
def username():
    return "testuser"

def test_username(username):
    assert username == "testuser"
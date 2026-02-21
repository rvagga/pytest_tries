
import pytest

@pytest.mark.smoke
def test_admin_login():
    user = "admin"
    valid = True
    assert valid

def test_user1_login():
    user = "user1"
    valid = True
    assert valid

@pytest.mark.xfail()
def test_guest_login():
    user = "guest"
    valid = False
    assert valid
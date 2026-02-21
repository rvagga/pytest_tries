#test_types.py

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_login_valid():
    assert True

@pytest.mark.regression
def test_login_invalid():
    assert False

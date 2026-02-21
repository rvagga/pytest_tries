#fixture scope ="module": список для 2 тестов

import pytest
@pytest.fixture(scope="module")
def data():
    return [1,2] 

def test_min(data):
    assert min(data) == 1
def test_max(data):
    assert max(data) == 2
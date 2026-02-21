#fixture с yield: data =[1,2], teardown print("Cleanup")

import pytest
@pytest.fixture()
def test_data():
    data = [1,2]
    yield #data
    print("Cleanup")
def test_yield(test_data):
    assert test_data == [1,2]



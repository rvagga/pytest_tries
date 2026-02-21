#авто-фикстура: @pytest.fixture(autouse=True) печатает "Start test"
#балуюсь yield
import pytest
@pytest.fixture(autouse=True)
def print_start():
    print("Start test")
    yield
    print("Finished")

def test_numbers():
    assert 1 + 1 == 2

def test_numbers_1():
    assert 2 + 2 == 4
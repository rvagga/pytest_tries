import pytest
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [2, 3, 4])
def test_x_less_than_y(x, y):
    if x < y:
        assert x < y
import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (9, 3, 3)
    ]
)
def test_division(a, b, expected):
    assert a / b == expected
import pytest

@pytest.mark.parametrize(
    "num,is_even_expected",
    [
        (2, True),
        (3, False)
    ]
)
def test_is_even(num, is_even_expected):
    def is_even(x):
        return x % 2 == 0

    assert is_even(num) == is_even_expected 
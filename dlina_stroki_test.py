import pytest

@pytest.mark.parametrize(
    "s,expected_len",
    [
        ("abc", 3),
        ("def", 3)
    ]
)
def test_string_length(s, expected_len):
    assert len(s) == expected_len 
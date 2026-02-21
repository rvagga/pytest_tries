
#test_unstable.py
import pytest

@pytest.mark.skip(reason="Фича не завершена")
def test_feature_a():
    assert 1 == 1

@pytest.mark.xfail(reason="Известный баг в продакшне")
def test_feature_b():
    assert 1 == 2 
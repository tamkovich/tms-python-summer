import pytest

from src.main import add


@pytest.mark.parametrize(
    'first_value, second_value, result',
    [
        (1, 2, 3),
        (200, 100, 300),
    ],
)
def test_simple(first_value, second_value, result):
    assert add(first_value, second_value) == result


@pytest.mark.parametrize(
    'failed_value',
    ((), {}, [], None, 'Some str', sum, object),
)
def test_bad_value(failed_value):
    """Test that add function returns 'Bad value' on {failed_value} value"""
    assert add(failed_value, 1) == 'Bad value'

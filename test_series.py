import pytest

PARAMS_TABLE_FIB = [
	(0, 0),
	(1, 1),
	(2, 1),
	(3, 2),
	(4, 3),
	(5, 5),
	(6, 8),
	(7, 13)
]
PARAMS_TABLE_LUCAS = [
	(0, 2),
	(1, 1),
	(2, 3),
	(3, 4),
	(4, 7),
	(5, 11),
	(6, 18),
	(7, 29)
]


@pytest.mark.parametrize("n, result", PARAMS_TABLE_FIB)
def test_fibonacci(n, result):
	from series import fibonacci
	assert fibonacci(n) == result


@pytest.mark.parametrize("n, result", PARAMS_TABLE_LUCAS)
def test_lucas(n, result):
	from series import lucas
	assert lucas(n) == result


@pytest.mark.parametrize("n, result", PARAMS_TABLE_FIB)
def test_sum_series(n, result):
    from series import sum_series
    assert sum_series(n) == result

@pytest.mark.parametrize("n, result", PARAMS_TABLE_LUCAS)
def test_sum_series_again(n, result):
    from series import sum_series
    assert sum_series(n,2,1) == result

@pytest.mark.parametrize("index", range(0,100))
def test_versus(index):
	from series import sum_series
	from series import fibonacci
	assert sum_series(index) == fibonacci(index)
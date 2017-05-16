import pytest

PARAMS_TABLE = [
	(0, 0),
	(1, 1),
	(2, 1),
	(3, 2),
	(4, 3),
	(5, 5),
	(6, 8),
	(7, 13)
]



@pytest.mark.parametrize("n, result", PARAMS_TABLE)
def test_fibonacci(n, result):
	from series import fibonacci
	assert fibonacci(n) == result


'''@pytest.mark.parametrize("m, n, result", PARAMS_TABLE)
def test_lucas(n, result):
	from series import lucas
	assert series(n) == result'''
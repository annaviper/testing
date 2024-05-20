import pytest


products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product


def test_one_plus_one():
    assert 1 + 1 == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        1 / 0
    assert 'division by zero' in str(e.value)

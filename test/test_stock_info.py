import pytest

from stock_info import metric


@pytest.mark.parametrize("roe, fcf, expected", [
    (20, 1000, 'A'),
    (20, 0, 'B1'),
    (10, 2000, 'B2'),
    (10, 0, 'C'),
    (2, 0, 'NG')])
def test_metric(roe, fcf, expected):
    assert metric(roe, fcf) == expected
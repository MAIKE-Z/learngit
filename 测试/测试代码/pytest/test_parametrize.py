import pytest
from datetime import datetime, timedelta


testdata=[
    (datetime(2020,3,16),datetime(2020,3,17),timedelta(-1)),
    (datetime(2020,3,17),datetime(2020,3,16),timedelta(1)),
]

@pytest.mark.parametrize("a,b,expected",testdata)
def test_timedistance_0(a,b,expected):
    diff=a-b
    assert diff==expected
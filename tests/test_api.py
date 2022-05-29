from re import S
from bb.api import quote


def test_quote():

    test = quote()

    assert type(test) == str
    assert len(test) > 0

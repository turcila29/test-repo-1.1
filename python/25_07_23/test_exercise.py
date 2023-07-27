import pytest
from exercise import maxlen


def test_one():
    assert maxlen.one("tiger", "computer") == "computer"
    assert maxlen.one("egg", "building") == "building"

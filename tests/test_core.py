# tests/test_core.py
from calculator import core
import pytest


def test_add():
    assert core.add(1, 2) == 3


def test_sub():
    assert core.sub(5, 3) == 2


def test_mul():
    assert core.mul(4, 2) == 8


def test_div():
    assert core.div(6, 3) == 2


def test_div_zero():
    with pytest.raises(ValueError):
        core.div(1, 0)

import pytest

from project_euler import sum_natural_multiples


def test_problem1():
    assert sum_natural_multiples(n=5, mults=[3, 5]) == 8
    assert sum_natural_multiples(n=9, mults=[3, 5]) == 23
    assert sum_natural_multiples(n=10, mults=[3, 5]) == 33

import pytest
from project_euler import fib_even_sum, is_prime, sum_natural_multiples, largest_prime_factor


def test_problem1():
    assert sum_natural_multiples(n=5, mults=[3, 5]) == 8
    assert sum_natural_multiples(n=9, mults=[3, 5]) == 23
    assert sum_natural_multiples(n=10, mults=[3, 5]) == 33


def test_problem2():

    assert fib_even_sum(10) == 10
    assert fib_even_sum(33) == 10
    assert fib_even_sum(88) == 44


def test_problem3():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(5) == 5
    assert largest_prime_factor(12) == 3


def test_is_prime():
    assert is_prime(11)
    assert not is_prime(10)

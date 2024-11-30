"""Tests the division examples."""

import random

from division import divide, divide_java, divide_python


def test_0_dividend() -> None:
    """Tests that a dividend of `0` returns `(0, 0)` regardless of divisor."""
    for divisor in range(1, 100):
        assert divide(0, divisor) == (0, 0)


def test_divide_by_1() -> None:
    """Tests that dividing `dividend` by a divisor of `1` returns `(dividend, 0)`."""
    for dividend in range(100):
        assert divide(dividend, 1) == (dividend, 0)


def test_17_divided_by_5() -> None:
    """Tests the 17 // 5 example from the notes."""
    assert divide(17, 5) == (3, 2)


def test_random_tests() -> None:
    """Tests random inputs to ensure consistency with Python's built-in operations."""
    random.seed(0)
    for _ in range(10_000):
        dividend = random.randrange(10_000_000)
        divisor = random.randrange(1, 10_000_000)
        assert divide(dividend, divisor) == divmod(dividend, divisor)


def test_java_division() -> None:
    """Tests the Java division sign adjustments."""
    m = 25
    n = 10
    # The assertions check:
    # divident == divisor * quotient + remainder.

    # Both positive.
    q, r = divide_java(m, n)
    assert (q, r) == (2, 5)
    assert m == n * q + r

    # Negative dividend.
    q, r = divide_java(-m, n)
    assert (q, r) == (-2, -5)
    assert -m == n * q + r

    # Negative divisor.
    q, r = divide_java(m, -n)
    assert (q, r) == (-2, 5)
    assert m == -n * q + r

    # Both negative.
    q, r = divide_java(-m, -n)
    assert (q, r) == (2, -5)
    assert -m == -n * q + r


def test_python_negative_mod() -> None:
    """Tests Python's modulus operator with negative right-hand-side input."""
    random.seed(0)
    for _ in range(10_000):
        dividend = random.randrange(-10_000_000, 10_000_000)
        divisor = random.randrange(-10_000_000, 0)
        assert -(-dividend % -divisor) == dividend % divisor


def test_python_division() -> None:
    """Tests the Python division algorithm on random inputs."""
    random.seed()
    for _ in range(10_000):
        dividend = random.randrange(-10_000_000, 10_000_000)
        divisor = random.randrange(-999_999, 10_000_000)
        if divisor == 0:
            divisor = -10_000_000
        assert divide_python(dividend, divisor) == divmod(dividend, divisor)

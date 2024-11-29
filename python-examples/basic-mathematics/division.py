"""Examples of the integer division."""


def divide(m: int, n: int) -> tuple[int, int]:
    """
    Returns the integer quotient `m // n` and remainder `m % n`.

    Here `m` is the dividend and `n` is the divisor.
    Requires `m >= 0 and n > 0`.
    """
    assert m >= 0 and n > 0
    count = 0
    while m >= n:
        count += 1
        m -= n
    return count, m


def divide_java(m: int, n: int) -> tuple[int, int]:
    """
    Returns `m / n, m % n` as implemented in Java.

    The returned quotient equals `abs(m) / abs(n)`, with the sign negative when one of
    `m` or `n` is negative. The remainder is given by `abs(m) % abs(n)`.

    Requires `n != 0`.
    """
    assert n
    sign = 1
    if m < 0:
        m = -m
        sign = -sign
    if n < 0:
        n = -n
        sign = -sign
    q, r = divide(m, n)
    return sign * q, r


def divide_python(m: int, n: int) -> tuple[int, int]:
    """
    Returns `m // n, m % n` as implements in Python

    TODO

    Requires n != 0.
    """
    return 0, 0

"""Examples of the integer division."""


def divide(m: int, n: int) -> tuple[int, int]:
    """
    Returns the integer quotient `m // n` and remainder `m % n`.

    Here `m` is the dividend and `n` is the divisor.
    Requires `m >= 0 and n > 0`.
    """
    assert m >= 0 and n > 0
    count = 0
    # m >= 0 and m + count * n equals the original value of m
    while m >= n:
        count += 1
        m -= n
    return count, m


def divide_java(m: int, n: int) -> tuple[int, int]:
    """
    Returns `m / n, m % n` as implemented in Java.

    The returned quotient equals `abs(m) / abs(n)`, with the sign negative when one of
    `m` or `n` is negative. The remainder is given by `abs(m) % abs(n)` and is
    negative when `m` is negative.

    Requires `n != 0`.
    """
    assert n
    q, r = divide(abs(m), abs(n))
    # The quotient is negative when exactly one of the inputs is negative.
    if (m < 0) ^ (n < 0):
        q = -q
    # The sign of the remainder depends only on the sign of the dividend.
    if m < 0:
        r = -r
    return q, r


def divide_python(m: int, n: int) -> tuple[int, int]:
    """
    Returns `m // n, m % n` as implemented in Python.

    Requires `n != 0`.
    """
    assert n
    q, r = divide(abs(m), abs(n))
    # If the signs are different, make the quotient negative and subtract 1 to account
    # for taking the floor when the remainder is nonzero.
    if (m < 0) ^ (n < 0):
        q = -q - (r != 0)
    # The returned remainder satisfies r == m - n * q.
    return q, m - n * q


def print_line() -> None:
    """Prints to `stdout` an example of division and remainder."""
    print(" ".join(f"{n: >3}" for n in range(-12, 12)))
    print(" ".join(f"{n % 7: >3}" for n in range(-12, 12)))
    print(" ".join(f"{n % -7: >3}" for n in range(-12, 12)))

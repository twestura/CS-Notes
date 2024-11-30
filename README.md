# CS-Notes
Notes for computer science topics, focused on algorithms and "interview-like" topics.

The notes themselves are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
The code examples in the repository are licensed under the [MIT License](https://github.com/twestura/CS-Notes/blob/main/LICENSE).

Coding examples focus on Python and Java, but we may reference Rust, Javascript/Typescript, OCaml, and Haskell from time to time.

## Introduction

## Installation, IDEs, and Programming Environment Setup

## Basic Mathematics

### Division, Remainder, and Modulus

In elementary school we learn an algorithm for long division, but the complexity of that algorithm may obscure that there is a "simplier" (albeit perhaps more tedius to carry out by hand) algorithm for determining the quotient and remainder: repeately subtract the divisor from the dividend, getting as close to $0$ as possible.
The count of the number of substractions is called the quotient, and the remaining number left over when we cannot perform another subtraction without going beyond $0$ is called the remainder.
The word "quotient" is derived from the Latin words *quot* meaning "how many" and *quotiens* meaning "how often" or "how many times."

That is, the division `m / n` of nonegative `m` and positive `n` is the count of how many times `n` can be subtracted from `m`.
For example, consider ${17 / 5}$:

$$17 \underbrace{- 5 - 5 - 5}_{3\text{ times}} = 2$$

Here we would reach a negative number were we to subtract another $5$, so we have a remainder of $2$.
We now write

$$3 \cdot 5 + 2 = 17.$$

The result of the integer division is two integers `q` and `r`, with `0 <= r < n`, such that `q * n + r = m`.
That is,
$$\text{quotient} \cdot \text{divisor} + \text{remainder} = \text{dividend}.$$

Division could be implemented by the following Python code.
Note this code aims to be obvious, not efficient.
```python
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
```

Let's analyze the loop invariant.
Let `m0` denote the initial value of `m`.
1. Initialization.
The function precondition is that `m0 >= 0`, and the variable `count` is initialized to `0`, satisfying `m0 == m + 0 * n`.
2. Maintenance.
Since `m >= n`, subtracting `n` from `m` still results in `m >= 0` at the end of the iteration.
Subtracting `n` from `m` but adding `1` to count results in the following:
```text
(m - n) * (1 + count) * n == m + (-n + n) + count * n == m + count * n == m0.
```
3. Postcondition.
The loop guard ends when `m < n`, and we have `0 <= m < n` since `m >= n` at the start of the previous iteration.
At the same time, `m0 == m + count * n`.
Hence `m` is the remainder, and `count` is the quotient.
4. Progress.
The precondition states that `n > 0`, and every iteration subtracts `n` from `m`, so eventually `m < n` as we're subtracting a positive number from another nonnegative number.

Different programming languages handle division and the remainder or modulus operator `%` in various ways for negative numbers.
Java treats `%` as a "remainder," whereas Python treats it as a modulus.
These operations coincide for ${m \ge 0}$ and ${n > 0}$, but differ for negative inputs.

In [Java](https://docs.oracle.com/javase/specs/jls/se23/html/jls-15.html#jls-15.17.2), the result of `/` is to take the division of the absolute values `abs(m) / abs(n)` and return the quotient with a sign depending on whether the number of negative numbers in the division is even or odd.
The remainder `%` is calculated by taking `abs(m) % abs(n)` and returning the result with the sign of `m`.
This method preserves the relationship that `n * q + r == m`, but the requirement on the remainder becomes `0 <= abs(r) < abs(n)`.

As a code example, we can use our other divison algorithm and account for the signs of the returned values.

```python
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
```

For Python, instead of rounding towards $0$, the division is floored.
That is, the result is always rounded down, which for negative numbers makes them even more negative.
For example, `5 / 2 == 2.5`.
As an integer divison, this quantity is rounded down to `5 // 2 == 2`.
Now, if instead we have a negative number and take `-5 / 2 == -2.5`, the result as an integer division still is rounded down to yield `-5 // 2 == -3`.
After determining the quotient, the remainder is set so that `r == m - q * n` is fulfilled.
<!-- TODO explain why the sign of the remainder is the sign of the divisor -->
<!-- TODO explain how this works... -->
For `n < 0`, we have `m % n == -(-m % -n)`.

```python
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
```

Python also provides the `divmod` function for calculating the quotient and remainder at the same time.
Other languages will likely have a compiler that handles this optimization step.

In my experience, Python's `%` is more useful for negative numbers than is Java's, as rare as those occurrences are.
The most typical examples are wrapping around indices of a list/array, or using floating-point numbers and doing some trigonometry modulo $2\pi$.
In Java, use [`Math.floorMod`](https://docs.oracle.com/en/java/javase/23/docs/api/java.base/java/lang/Math.html#floorMod(int,int)) to get the Python behavior.

The [Wikipedia page for the modulo operation](https://en.wikipedia.org/wiki/Modulo) has a nice table detailing how different programming languages implement `%` and provide the operation.
See also [this post](https://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html) about the design of Python's divison.

## Asymptotic Complexity
## Bit Twiddling
## Binary Search
## Sorting Algorithms
## Linked Lists
## Trees
## Hash Tables
## Graph Algorithms
## Divide and Conquer Algorithms
## Greedy Algorithms
## Dynamic Programming
## Computability Theory
## Prime Numbers
## Combinations and Permutations

# CS-Notes
Notes for computer science topics, focused on algorithms and "interview-like" topics.

The notes themselves are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
The code examples in the repository are licensed under the [MIT License](https://github.com/twestura/CS-Notes/blob/main/LICENSE).

Coding examples focus on Python and Java, but we may reference Rust, Javascript/Typescript, OCaml, and Haskell from time to time.

## Introduction

## Installation, IDEs, and Programming Environment Setup

## Basic Mathematics

### Division, Remainder, and Modulus

The division `m / n` of positive integers `m` and `n` is the count of the number of times `n` is subtracted from `m` to reach `0`.
If we repeatedly subtract but hit a value where the next subtraction would result in a negative number, we stop and call the remaining number the remainder.

For example, consider&nbsp;${17 / 5}$:
$$17 \underbrace{- 5 - 5 - 5}_{3\text{ times}} = 2$$
Here we would reach a negative number were we to subtract another&nbsp;$5$, so we have a remainder of&nbsp;$2$.
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
    while m >= n:
        count += 1
        m -= n
    return count, m
```

Different programming languages handle the remainder or modulus operator `%` in various ways.
Java treats it as a "remainder," whereas Python treats it as a modulus.
These operations coincide for&nbsp;${m \ge 0}$ and&nbsp;${n > 0}$, but differ for negative inputs.
<!-- TODO explain difference -->

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

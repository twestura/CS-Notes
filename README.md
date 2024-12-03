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

The result of the integer division is two integers `q` and `r`, with `0 <= r < n`, such that `q * n + r == m`.
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

### Logarithms

Logarithms were introduced in the early 1600's independently by two mathematicians: the Scottsman John Napier and the Swiss Jost Bürgi.
And oh boy, John Napier apparently was quite the character.
He was accused of being a magician and necromancer, with a black rooster as his summoning familiar.

Anyway, Napier was the one who created the word logarithm, smashing together the Greek words *logos*, roughly meaning ratio, or calculation, and *arithmos* meaning number.
The logarithm is essentially the "calculation-number" that originally was used to enable mathematicians, astronomers, and other interested folk to speed up the process of performing multiplications and other calculations.

Adding numbers by hand is a process that is linear in the number of digits: just pair them up, add the pairs from right to left, potentially carrying a 1 when necessary.
But multiplication is quadratic in the number of digits: each digit in the "top" number is multiplied by each digit in the "bottom" number, and then all of these products are summed together.
Rather than needing to perform these calculations every time, logarithm tables were written that enabled the user to look up the numbers they wanted to multiply, map the numbers to their logarithms, add the logarithms, and then look up the exponentiation of the sum to get the answer.

$$xy = \log_b{xy} = \log_b{x} + \log_b{y} = b^{\log_b{x} + \log_b{y}}.$$

The process of a multiplication was replaced by three table lookups and one addition.

For real numbers ${x, b > 0}$ with ${b \ne 1}$, the real number $y$ such that ${x = b^y}$ is called the base $b$ logarithm of $x$, and we write ${\log_b{x} = y}$.
When $y$ is an integer, the logarithm is the number of times $b$ is multiplied by itself to equal $x$.

For example:

$$2^4 = \underbrace{2 \cdot 2 \cdot 2 \cdot 2}_{4 \text{ times}} = 16; \qquad \log_2{16} = 4.$$

But this equation can be interprete another way.
We can view the logarithm as giving the number of times we can divide $16$ by $2$ to get all the way down to $1$.

$$
    \begin{align*}
        16 / 2 &= 8,\\
        8 / 2 &= 4,\\
        4 / 2 &= 2,\\
        2 / 2 &= 1.
    \end{align*}
$$

This interpretation is analogous to our description of division as the number of subtractions performed in order to reach $0$.
And the count of the number of divisions to reach $1$ is how we commonly use algorithms in analyzing the running time of divide and conquer algorithms: we divide the problem into subproblems, and the logarithm gives the "height" of the stack of subproblems.

There are two important properties of logarithms:

- They act as an inverse to exponentiation.
- They exchange multiplication and addition.

The other properties of logarithms are derived from these properties.

The two inverse properties follow directy from the definition:

- $\log_b{b^x} = x$. The exponent to which $b$ is raised to obtain $b^x$ is $x$.
- $b^{\log_b{x}} = x$. By definition $\log_b{x}$ is the exponent to which $b$ is raised to obtain $x$. Raising $b$ to that exponent indeed yields $x$.

When performing calculations by hand, it is common to "cross out" the base and logarithm when either exponentiation or taking the logarithm of both sides of an equation.
Be careful, though, that we understand the inverse property we're applying, and not just mechanically crossing out notation without thinking about why it's possible to do so.

From here we can plug in the values ${x = 0}$ and ${x = 1}$ to obtain two corollaries:

- $\log_b{1} = \log_b{b^0} = 0,$
- $\log_b{b} = \log_b{b^1} = 1.$

Next is the product rule.
For $b$, $x$, and $y$ positive real numbers with ${b \ne 1}$:

$$\log_b{xy} = \log_b{x} + \log_b{y}.$$

To prove this rule, we use the inverse laws and the property of exponentiation that ${b^x b^y = b^{x + y}}$.
We perform the following calculation to obtain the rule:

$$xy = b^{\log_b{x}} b^{\log_b{y}} = b^{\log_b{x} + \log_b{y}}.$$

For integer exponents, this rule is stating "the number of times we multiply $b$ to get $xy$ is the sum of the numbers of times to get $x$ and $y$ individually."
Writing this out, we can see how the associativity of multiplication plays a role:

<!-- Note GitHub cannot seem to format multiple underbraces on the same line. -->
$$xy = \overbrace{\underbrace{\left(b\cdots{}b\right)}_{\log_b{x}\text{ times }}\underbrace{\left(b\cdots{}b\right)}_{\log_b{y}\text{ times }}}^{\log_b{x} + \log_b{y}\text{ times}}$$

Next is the "power rule," which states we can remove an exponent from inside of a log and place it as a coefficient outside of the log.
Let $b$, $x$, and $y$ be real numbers, ${b, x > 0}$, and ${b \ne 1}$.
Then

$$\log_b{x^y} = y \log_b{x}.$$

To show this rule, we use the property that ${{(b^x)}^y = b^{xy}}$:

$$x^y = {\left(b^{\log_b{x}}\right)}^y = b^{y\log_b{x}}.$$

In particular, we can extract roots.
For a positive integer~$n$, appliying this rule yields

$$\log_b{\sqrt[n]{x}} = \frac{1}{n} \log_b{x}.$$

Combining with the product rule, we obtain the quotient rule for positive numbers $b$, $x$, and $y$ with ${b \ne 1}$:

$$\log_b{\frac{x}{y}} = \log_b{x} - \log_b{y}.$$

To see this, note that ${\frac{x}{y} = xy^{-1}}$ and apply the previous two laws.

$$\log_b{\frac{x}{y}} = \log_b{xy^{-1}} = \log_b{x} + \log_b{y^{-1}} = \log_b{x} - \log_b{y}.$$

And finally we have the change of base formula.
Let $b$, $x$, and $y$ be positive numbers with ${b \ne 1}$ then for all positive real numbers ${a \ne q}$, we have

$$\log_b{x} = \frac{\log_a{x}}{\log_a{b}}.$$

We prove this formula as follows:

$$x = b^{\log_b{x}} = {(a^{\log_a{b}})}^{\log_b{x}} = a^{\log_b{x} \log_a{b}}.$$

Therefore

$$\log_a{x} = \log_b{x} \log_a{b},$$

and dividing by $\log_a{b}$ gives the desired formula.
Note this division is always possible since we require ${b \ne 1}$, and hence ${\log_a{b} \ne 0}$.

As a corollary, for postive nonzero real numbers $a$ and $b$, we can plug in $a$ for in in the formula to obtain:

$$\log_b{a} = \frac{1}{\log_a{b}},$$

giving a formula for "swapping" the base and the argument.

And one final property.
Let $b$, $x$, and $y$ be real numbers, ${b, x > 0}$, ${b \ne 1}$, and ${y \ne 0}$.
Then

$$\log_{b^y}{x} = \frac{1}{y} \log_b{x}.$$

To prove this property, note

$$x = {(b^y)}^{\log_{b^y}{x}} = b^{y \log_{b^y}{x}}.$$

This equation gives us

$$\log_{b}{x} = y\log_{b^y}{x}.$$

Dividing both sides by $y$, which we can do since we assumed $y$ is nonzero, yields the desired form.
Of particular use is the case ${y = -1}$:

$$\log_{\frac{1}{b}}{x} = -\log_b{x}.$$

The following table summarizes the important properties of logarithms.

| Log properties | Corollaries |
| -------------- | ----------- |
| $$b^{\log_b{x}} = x$$ | $$\log_b{1} = 0$$ |
| $$\log_b{b^x} = x$$ | $$\log_b{b} = 1$$ |
| $$\log_b{xy} = \log_b{x} + \log_b{y}$$ | $$\log_b{\frac{x}{y}} = \log_b{x} - \log_b{y}$$ |
| $$\log_b{x^y} = y\log_b{x}$$ | $$\log_b{\sqrt[n]{x}} = \frac{1}{n}\log_b{x}$$ |
| $$\log_{b^y}{x} = \frac{1}{y}\log_b{x}$$ | $$\log_{\frac{1}{b}}{x} = -\log_b{x}$$ |
| $$\log_b{x} = \frac{\log_a{x}}{\log_a{b}}$$ | $$\log_b{a} = \frac{1}{\log_a{b}}$$ |

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

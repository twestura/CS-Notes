"""Tests the maximum points problem."""

import math

from atan import max_points, max_points_binary

HALF_PI = math.pi / 2.0


def test_single() -> None:
    """Tests a single point."""
    assert 1 == max_points([(1, 2)], HALF_PI)


def test_double() -> None:
    """Tests two points within the arc."""
    assert 2 == max_points([(1, 2), (2, 1)], HALF_PI)


def test_split() -> None:
    """Tests two points with a max of 1 in the arc."""
    assert 1 == max_points([(1, 1), (-1, -1)], HALF_PI)


def test_mulitple_in_arc() -> None:
    """Tests multiple points within the arc."""
    assert 5 == max_points([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)], HALF_PI)


def test_mixture() -> None:
    """Tests points within and outside the arc."""
    assert 5 == max_points(
        [
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (-1, -1),
            (-1, -2),
            (-1, -3),
            (-1, -4),
            (-1, -5),
        ],
        HALF_PI,
    )


def test_tight_mixture() -> None:
    """Tests the arc selects the cluster of points within a small angle."""
    assert 4 == max_points(
        [
            (1, 1.1),
            (1, 1.2),
            (1, 1.3),
            (1, 1.4),
            (-1, -1),
            (-1, -2),
            (-1, -3),
            (-1, -4),
            (-1, -5),
        ],
        math.pi / 12.0,
    )


def test_empty_list() -> None:
    """Tests that an empty list of points returns 0."""
    assert 0 == max_points([], HALF_PI)


def test_negative_angle() -> None:
    """Tests that a negative angle includes no points."""
    assert 2 == max_points([(1, 1), (1, 2), (-1, -1)], -HALF_PI)
    assert 2 == max_points([(1, 1), (1, 2), (-1, -1)], HALF_PI)


def test_single_point_zero_angle() -> None:
    """Tests a single point is returend with an angle of zero."""
    assert 1 == max_points([(1, 1)], 0.0)


def test_many_points_zero_angle() -> None:
    """Tests a line of points with an angle of zero."""
    assert 9 == max_points([(i, i) for i in range(1, 10)] + [(-1.0, -1.0)], 0.0)


# TODO more test cases
# TODO parametrize tests for the binary search case
# TODO test both implementation agree on random inputs

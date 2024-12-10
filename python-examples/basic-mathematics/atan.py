"""An example interview question."""


import math


def max_points(
    points: list[tuple[float, float]], angle: float, x0: float = 0, y0: float = 0
) -> int:
    """
    Returns the maximum number of points within `angle` at `(x0, y0)`.

    The intuition is to place a camera at point `(x0, y0)`. The camera
    cannot move but can rotate, and has a field of view of `angle`. The
    function returns the maximum number of points visible in the
    camera's viewing angle by rotating the camera.

    Every point in `points` that equals `(x0, y0)` is considered always
    visible. That is, the camera always sees the points at the same
    coordinate as itself.

    Points do not obscure each other. If multiple points are in a
    straight line from the camera, all of them are visible at once.

    If `angle` is zero, then individual points, as well as multiple
    points in a straight line from the camera, are considered visible.

    If `angle` is negative, the same number of points is returned as
    though `angle` were positive.

    If `angle` is greater than or equal to `math.tau`, points may be
    counted multiple times. This value is treated as
    `divmod(angle, math.tau)` where the quotient is the number of times
    all points are repeated, and the remainder serves as the angle for
    gathering the largest number of points.

    Realistically the angle for a camera would be constrained to
    `(0, math.tau)` at least, but considering larger angles makes for a
    fun problem. :)
    """
    # The number of points at the camera's position.
    num_origin = sum(x0 == x and y0 == y for x, y in points)
    # Non-origin points converted to the angle they make with the x-axis, with the
    # angle value in the range `[0, math.tau)`.
    angles = sorted(
        math.atan2(y - y0, x - x0) % math.tau for x, y in points if x != x0 or y != y0
    )
    n = len(angles)  # The number of non-origin points included in `angles`.

    def get_angle(i: int) -> float:
        return math.tau + angles[i % n] if i >= n else angles[i]

    num_repeats, angle = divmod(abs(angle), math.tau)
    num_repeats = int(num_repeats)  # The quotient of the `divmod` is an integer.
    max_points = 0
    size = 1
    # TODO loop invariant
    for left, theta in enumerate(angles):
        while get_angle(left + size) - theta <= angle:
            size += 1
        # Terminate early if all points are visible.
        if size == n:
            return (num_repeats + 1) * (n + num_origin)
        max_points = max(max_points, size)
        size -= 1
    return max_points + num_origin + num_repeats * (n + num_origin)

    # TODO also consider the binary search approach


def max_points_binary(
    points: list[tuple[float, float]], angle: float, x0: float = 0, y0: float = 0
) -> int:
    """
    See `max_points`.

    This function is an alternative implementation that uses a binary
    search in the loop instead of a two-pointer approach.
    """
    raise Exception()

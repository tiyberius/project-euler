from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', ['x', 'y'])


def solve_problem():
    laser_origin = Point(0.0, 10.1)
    laser_destination = Point(1.4, -9.6)
    bounces = 0
    while True:
        new_laser_destination = bounce_laser(laser_origin, laser_destination)
        bounces += 1
        laser_origin = laser_destination
        laser_destination = new_laser_destination
        if laser_did_escape(new_laser_destination):
            break
    return bounces


def bounce_laser(laser_origin, laser_destination):
    """
    Args:
        laser_origin (Point): Where the laser is coming from
        laser_destination (Point): Where the laser hits the inside of the white cell

    Returns:
        Point: The next point the laser hits inside the white cell

    Examples:
        >>> bounce_laser(Point(0.0, 10.1), Point(1.4, -9.6))
        Point(x=-3.990597619361617, y=-6.024991498863843)
        >>> bounce_laser(Point(1.4, -9.6), Point(-3.990597619361617, -6.024991498863843))
        Point(x=0.32458287808384617, y=9.97890694520293)
    """
    incoming_beam_slope = slope(laser_origin, laser_destination)
    tangent_slope = slope_of_ellipse_tangent_at(laser_destination)
    reflecting_beam_slope = slope_of_reflecting_beam(incoming_beam_slope, tangent_slope)
    reflecting_beam_intercept = calculate_intercept(reflecting_beam_slope, laser_destination)
    solution1, solution2 = solve_quadratic_equation(reflecting_beam_slope,
                                                    reflecting_beam_intercept)
    # of the two solutions we get from solving the quadratic equation, we want the furthest one
    # away from where the laser bounced because we know the laser is NOT going to end up where it
    # started
    if abs(solution1 - laser_destination.x) > abs(solution2 - laser_destination.x):
        new_laser_destination_x = solution1
    else:
        new_laser_destination_x = solution2
    new_laser_destination_y = (reflecting_beam_slope * new_laser_destination_x +
                               reflecting_beam_intercept)
    return Point(new_laser_destination_x, new_laser_destination_y)


def solve_quadratic_equation(line_slope, line_intercept):
    """
    This code in this function is the result of some heavily reduced math that solves for the two
    potential x co-ordinates where the ellipse and a given line intersect.

    Args:
        line_slope (float): The slope of the line that is intersecting with the ellipse
        line_intercept (float): The intercept of the line that is intersecting with the ellipse

    Returns:
        float, float: Since there are two solutions to any quadratic equation, we'll give you both
            and let you decide which one you want :)

    Examples:
        >>> solve_quadratic_equation(-0.663193351382, -8.67152930807)
        (1.3999999999961497, -3.990597619359253)
        >>> solve_quadratic_equation(3.70874369068, 8.77511224401)
        (0.32458287808298875, -3.990597619365363)
    """
    a = 4 + line_slope ** 2
    b = 2 * line_slope * line_intercept
    c = (line_intercept ** 2) - 100

    solution1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    solution2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    return solution1, solution2


def calculate_intercept(slope, point):
    """
    Args:
        slope (float): The slope of a line
        point (Point): Any point on the line

    Returns:
        float: The point at which the line intersects the y-axis

    Examples:
        >>> calculate_intercept(3, Point(15, 50))
        5.0
        >>> calculate_intercept(1, Point(0, 0))
        0.0
        >>> calculate_intercept(-2, Point(-5, 8))
        -2.0
    """
    return float(point.y) - float(slope) * float(point.x)


def slope_of_reflecting_beam(incoming_beam_slope, tangent_slope):
    """
    Args:
        incoming_slope (float): The slope of an incoming laser

    Returns:
        float: The slope of the outgoing laser after it has bounced

    Examples:
        >>> slope_of_reflecting_beam(-14.0714285714, 0.583333333333)
        -0.6631933513829037
        >>> slope_of_reflecting_beam(-0.663193351382, -2.64936315353)
        3.708743690700296
    """
    tangent_of_incoming_beam = ((incoming_beam_slope - tangent_slope) /
                                (1 + incoming_beam_slope * tangent_slope))
    slope_of_reflecting_beam = ((tangent_slope - tangent_of_incoming_beam) /
                                (1 + tangent_of_incoming_beam * tangent_slope))
    return slope_of_reflecting_beam


def slope_of_ellipse_tangent_at(point):
    """
    Args:
        point (Point): Calculate the slope of the ellipse tangent at this point

    Returns:
        float: The slope of the ellipse tangent at the given point

    Examples:
        >>> slope_of_ellipse_tangent_at(Point(1.4, -9.6))
        0.5833333333333334
        >>> slope_of_ellipse_tangent_at(Point(0, -10))
        0.0
        >>> slope_of_ellipse_tangent_at(Point(-5, 0))
        inf
    """
    try:
        return -4 * (float(point.x) / float(point.y))
    except ZeroDivisionError:
        return float('inf')


def slope(first_point, second_point):
    """
    Args:
        first_point (Point): Line's start
        second_point (Point): Line's end

    Returns:
        float: The slope of a line between the two points

    Examples:
        >>> slope(Point(0, 0), Point(1, 5))
        5.0
        >>> slope(Point(0, 0), Point(-50.0, 1))
        -0.02
        >>> slope(Point(0, 0), Point(0, 1))
        inf
        >>> slope(Point(0, 0), Point(1, 0))
        -0.0
    """
    try:
        return ((float(first_point.y) - float(second_point.y)) /
                (float(first_point.x) - float(second_point.x)))
    except ZeroDivisionError:
        return float('inf')


def laser_did_escape(reflection_point):
    """
    Args:
        reflection_point (Point): The point at which the laser bounces off the inside of the ellipse

    Returns:
        bool: Returns True if the laser escaped, False if not

    Examples:
        >>> laser_did_escape(reflection_point=Point(0, 10.1))
        True
        >>> laser_did_escape(reflection_point=Point(1.4, -9.6))
        False
    """
    if (reflection_point.x < 0.01) and (reflection_point.x >= -0.01) and (reflection_point.y > 0):
        return True
    return False

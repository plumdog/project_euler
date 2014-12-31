#!/usr/bin/env python3

#import itertools
import fractions

def main(size):
    """Count the number of right-angle triangles that can be made on a
    grid of `size` squares.

    """

    # with right angle at the origin
    count = size * size

    # with the right angle on the x axis or on the y axis
    count += 2 * size * size

    for x in range(1, size + 1):
        for y in range(1, size + 1):
            count += num_perp_points(size, (x, y))

    return count

def num_perp_points(size, point):
    """Returns the number of points within a grid of `size` squares for
    which the angle made at point with the origin is a right angle.

    """

    # try each column and work out the y-value that would be needed
    # for a right angle. Check if it is an integer and within the
    # required range.

    # gradient = -1 / (point[1]/point[0]) = -point[0]/point[1]
    # y = mx + c
    # m = -point[0]/point[1]
    # x = point[0] => y = point[1]
    #              => point[1] = (-point[0]/point[1])*point[0] + c
    #              => c = (point[0]^2 + point[1]^2)/point[1]
    # so line is
    # y = (-point[0]/point[1])x + (point[0]^2 + point[1]^2)/point[1]

    m = fractions.Fraction(-point[0], point[1])
    c = fractions.Fraction(point[0]*point[0] + point[1]*point[1], point[1])

    count = 0
    for x in range(0, size + 1):
        if x == point[0]:
            continue
        y = m * x + c
        if (0 <= y <= size) and (y.numerator % y.denominator == 0):
            count += 1
    return count
        
        

    

if __name__ == '__main__':
    print(main(50))

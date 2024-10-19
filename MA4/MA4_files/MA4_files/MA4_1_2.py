"""
Solutions to module 4
Review date:
"""

student = "Anton Ahlzén"
reviewer = ""


import math
import math as m
import random as r
import functools


def sphere_volume(n, dimensions):
    # n is the number of coordinates
    # d is the number of dimensions of the sphere

    # distances = [(functools.reduce(lambda x,y: x+y, map(lambda x: x**2, [r.uniform(-R/2, R/2) for d in range(dimensions)]))) for point in range(n)]

    squared_distances = []
    for _ in range(n):
        point = [r.uniform(-1, 1) for dim in range(dimensions)]
        point_sqrd = list(map(lambda x: x**2, point))
        distance_squared = functools.reduce(lambda x,y: x+y, point_sqrd)
        squared_distances.append(distance_squared)

    n_c = len(list(filter(lambda x: x <= 1, squared_distances)))
    volume = (n_c * 2**dimensions) / n
    return volume


def hypersphere_exact(n, d):
    return math.pi**(d/2) / math.gamma(d/2 + 1)


def main():
    n = 100000
    d = 3
    approx_2d = sphere_volume(n, d)
    exact_2d = hypersphere_exact(n, d)
    print('Approximation for 2d: ', approx_2d)
    print('Exact for 2d: ', exact_2d)
    print('Fraction: ', exact_2d / approx_2d)

    print()
    d = 11
    approx_11d = sphere_volume(n, d)
    exact_11d = hypersphere_exact(n, d)
    print('Approximation for 11d: ', approx_11d)
    print('Exact for 11d: ', exact_11d)
    print('Fraction: ', exact_11d / approx_11d)


if __name__ == '__main__':
    main()
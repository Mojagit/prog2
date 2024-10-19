"""
Solutions to module 4
Review date:
"""

student = "Anton Ahlzén"
reviewer = ""

import math
import random as r
import matplotlib.pyplot as plt


def approximate_pi(n):
    # Write your code here
    n_c_xlist = []
    n_c_ylist = []
    n_xlist = []
    n_ylist = []

    n_c = 0
    for point in range(n):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1.0:
            n_c += 1
            n_c_xlist.append(x)
            n_c_ylist.append(y)
        else:
            n_xlist.append(x)
            n_ylist.append(y)
    plt.plot(n_c_xlist, n_c_ylist, 'ro', )
    plt.plot(n_xlist, n_ylist, 'bo')
    plt.savefig(f"pi_{n}.png")
    plt.clf()

    pi_approx = 4 * n_c / n
    print(pi_approx)
    print(math.pi)
    return pi_approx


def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)


if __name__ == '__main__':
    main()
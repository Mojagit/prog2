
"""
Solutions to module 4
Review date:
"""

student = "Anton Ahlzén"
reviewer = ""

import math
import random
import functools
from time import perf_counter as pc
from time import sleep
import concurrent.futures as future
import multiprocessing as mp



def sphere_volume(n, dimensions):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere

    squared_distances = []
    for _ in range(int(n)):
        point = [random.uniform(-1, 1) for dim in range(dimensions)]
        point_sqrd = list(map(lambda x: x ** 2, point))
        distance_squared = functools.reduce(lambda x, y: x + y, point_sqrd)
        squared_distances.append(distance_squared)

    n_c = len(list(filter(lambda x: x <= 1, squared_distances)))
    volume = (n_c * 2**dimensions) / n
    return volume


def hypersphere_exact(n, d):
    return math.pi**(d/2) / math.gamma(d/2 + 1)


# parallel code - parallelize for loop
def sphere_volume_parallel1(n, dimensions, np):
    # using multiprocessor to perform 10 iterations of volume function
    with future.ProcessPoolExecutor() as ex:
        processes = []
        parallel_result_loop = 0
        for _ in range(np):
            processes.append(ex.submit(sphere_volume, n, dimensions))
        for p in processes:
            parallel_result_loop += p.result()
        parallel_result_loop /= np
    return parallel_result_loop


# parallel code - parallelize actual computations by splitting data

def sphere_volume_parallel2(n, dimensions, np):
    with future.ProcessPoolExecutor() as ex:
        processes = []
        result = 0
        partial_n = int(n / np)
        for _ in range(np):
            processes.append(ex.submit(sphere_volume, partial_n, dimensions))
        for p in processes:
            result += p.result()
        result /= np
    return result


def main():
    n = 100000
    d = 11

    # part 1 -- parallelization of a for loop among 10 processes -----
    start121 = pc()
    normal_result_loop = 0
    for y in range(10):
        normal_result_loop += sphere_volume(n, d)
    normal_result_loop /= 10
    end121 = pc()

    start131 = pc()
    parallel_result_loop = sphere_volume_parallel1(n, d, 10)
    end131 = pc()

    # ----------------------------------------------------------------

    # part 2 -- parallelization of data divided among 10 processes

    start122 = pc()
    normal_result = sphere_volume(n, d)
    end122 = pc()

    np = 8
    start132 = pc()
    parallel_result = sphere_volume_parallel2(n, d, np)
    print(parallel_result)
    end132 = pc()

    print("1.3.1: Parallelization of 'for' loop -------------------------------")
    print()
    print('normal result: ', normal_result_loop)
    print('parallel result: ', parallel_result_loop)
    print('exact result: ', hypersphere_exact(n, d))
    print()
    print('time for normal: ', end121-start121)
    print('time for parallel: ', end131-start131)
    print('--------------------------------------------------------------------')

    print()

    print("1.3.2: Parallelization of divided data -----------------------------")
    print()
    print('normal result: ', normal_result)
    print('parallel result: ', parallel_result)
    print('exact result: ', hypersphere_exact(n, d))
    print()
    print('time for normal: ', end122-start122)
    print('time for parallel: ', end132-start132)
    print('--------------------------------------------------------------------')



if __name__ == '__main__':
    main()



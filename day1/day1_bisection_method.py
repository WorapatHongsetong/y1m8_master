import math

def bisection_method(func, a, b, p=1e-10):

    f_m = None
    mid_point = None
    interval = (a,b)
    iteration = 1
    while abs(interval[0] - interval[1]) >= p:
        mid_point = (interval[0] + interval[1])/2
        f_m = func(mid_point)

        print(f"calculating, mid point = {mid_point}, iter = {iteration}")

        if f_m == 0:
            break
        elif f_m * func(interval[0]) < 0:
            interval = (interval[0], mid_point)
        else:
            interval = (mid_point, interval[1])

        iteration += 1

    return mid_point

def iteration_of_bisection_method(a, b, p=1e-1):

    interation = math.log2((b - a)/ p)

    return interation
    

def f(x):
    return x ** 3


if 1:
    print(f"mid point = {bisection_method(f, -1, 10)}")
    print(f"approx iter = {iteration_of_bisection_method(-1, 10, 1e-10)}")
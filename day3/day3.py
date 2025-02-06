def contraction_test(func, start, end, max_iter=1000,  p=1e-10):
    x = start
    for i in range(max_iter):
        if abs(func(x) - x) <= p:
            return x
        if i > 0 and abs(x_prev - x) <= p:
            return x
        print(f"Iteration: {i}, Value: {x}")

        x_prev = x
        x += (end - start)/max_iter


def f(x):
    return x**2 -x -2

def dg_1(x):
    return 2*x

def dg_2(x):
    return 1/(2 * (x+2)**0.5)

def dg_3(x):
    return -2/(x**2)

def dg_4(x):
    return -1/600 * (x**2 -x -2) + x

# fixed_points = []
# fixed_points.append(contraction_test(dg_1, -1/2, p=1e-4))
# print(fixed_points)
# fixed_points.append(contraction_test(dg_2, -1, p=1e-4))
# print(fixed_points)
# fixed_points.append(contraction_test(dg_3, 2**0.5, p=1e-4))
# print(fixed_points)

print(contraction_test(dg_4, 1, 3, 1000, p=1e-4))
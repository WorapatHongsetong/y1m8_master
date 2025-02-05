def contraction_test(func, x_0, p=1e-10):
    x = x_0
    iterations = 1
    while True:
        if abs(func(x) - x) <= p:
            return x
        print(f"Iteration: {iterations}, Value: {x}")
        x += p
        iterations += 1

def f(x):
    return x**2 -x -2

def dg_1(x):
    return 2*x

def dg_2(x):
    return 1/(2 * (x+2)**0.5)

def dg_3(x):
    return -2/(x**2)

def dg_4(x):
    return -1/6 * (x**2 -x -2) + x

# fixed_points = []
# fixed_points.append(contraction_test(dg_1, -1/2, p=1e-4))
# print(fixed_points)
# fixed_points.append(contraction_test(dg_2, -1, p=1e-4))
# print(fixed_points)
# fixed_points.append(contraction_test(dg_3, 2**0.5, p=1e-4))
# print(fixed_points)

print(contraction_test(dg_4, 1, p=1e-4))
def bisection_method(func, a, b, p=1e-10):

    f_m = None
    mid_point = None
    interval = (a,b)
    iteration = 1
    while abs(interval[0] - interval[1]) >= p:
        mid_point = (interval[0] + interval[1])/2
        f_m = func(mid_point)

        print(f"calculating: mid point = {mid_point}, iter = {iteration}")

        if f_m == 0:
            break
        elif f_m * func(interval[0]) < 0:
            interval = (interval[0], mid_point)
        else:
            interval = (mid_point, interval[1])

        iteration += 1

    return mid_point

def subsection_bisection_method(func, a, b, roots=set(), p=1e-10):

    mid_point = (a + b)/2
    ans_roots = roots

    if func(a) * func(b) >= 0:
        ans_roots = ans_roots | (subsection_bisection_method(func, a, mid_point, ans_roots, p))
        ans_roots = ans_roots | (subsection_bisection_method(func, mid_point, b, ans_roots, p))

    else:
        ans_roots = ans_roots | {bisection_method(func, a, b, p)}

    return ans_roots


def f(x):
    return x**4 + 3*x**3 + x**2 - 2*x - 0.5

print(subsection_bisection_method(f, -3, 1))

import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import imageio

data = []

def bisection_method(func, a, b, p=1e-10):
    f_m = None
    mid_point = None
    interval = (a,b)
    iteration = 1
    while abs(interval[0] - interval[1]) >= p:
        mid_point = (interval[0] + interval[1])/2
        f_m = func(mid_point)

        print(f"calculating: mid point = {mid_point}, iter = {iteration}")
        data.append(mid_point)

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

def create_animation():
    x_roots = data
    y_roots = [f(i) for i in data]

    x = np.linspace(-4, 3, 200)
    y = f(x)

    plt.ylim((-3, 3))
    plt.plot(x, y)
    plt.axhline(color="black")

    output_dir = './day2/animation_image'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(len(x_roots)):
        plt.scatter(x_roots[i], y_roots[i], color="red")
        plt.savefig(f'{output_dir}/plot_image{i:03}.png')

    output_gif = "./day2/day2_animation.gif"
    image_files = sorted([f for f in os.listdir(output_dir) if f.endswith(('.png', '.jpg', '.jpeg'))])

    images = []
    for img_file in image_files:
        img_path = os.path.join(output_dir, img_file)
        img = Image.open(img_path)
        images.append(img)

    images[0].save(output_gif, save_all=True, append_images=images[1:], duration=200, loop=0)
    print(f"GIF saved as {output_gif}")

create_animation()

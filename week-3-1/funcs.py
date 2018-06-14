import numpy as np
import matplotlib.pylab as plt

def f(x):
    return np.sin(x / 5.0) * np.exp(x / 10.0) + 5 * np.exp(-x / 2)


def int_f(x):
    return int(f(x))

def para(x):
    return x**2

def plot_func(g, bounds):
    x = np.arange(bounds[0], bounds[1], 0.1)
    plt.plot(x, [g(i) for i in x])
    plt.show()


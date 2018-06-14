import numpy as np
import scipy
import scipy.linalg
from matplotlib import pylab as plt


def f(x):
    return np.sin(x / 5.0) * np.exp(x / 10.0) + 5 * np.exp(-x / 2)


def create_matrix(points, degree):
    # left = 1
    # right = 16
    # x = range(left, right, step)
    x = points
    s = []
    y = []
    for p in x:
        y.append(f(p))
        s.append([float(p)**i for i in range(degree+1)])
    b = np.array(y)[:, np.newaxis]
    A = np.matrix(s)
    return A, b


def find_polynom(A, b):
    c = scipy.linalg.solve(A, b)
    coef = [c[i][0] for i in range(c.size)]
    print coef
    def g(x):
        y = 0
        for i, c in enumerate(coef):
            y += x ** i * c
        return y
    return g


def plot_polynom(g):
    x = np.arange(1, 15.1, 0.1)
    # x = range(1, 15.1, 0.1)
    # print x[0], g(x[0]), f(x[0])
    plt.plot(x, [g(i) for i in x], x, [f(i) for i in x])
    plt.show()


if __name__ == "__main__":
    # points = [1, 15]
    # points = [1, 8, 15]
    points = [1, 4, 10, 15]
    # points = [1, 3, 4, 6, 8, 11, 15]
    points = map(float, points)
    A, b = create_matrix(points, len(points)-1)
    g = find_polynom(A, b)
    plot_polynom(g)


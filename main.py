import numpy as np
import scipy
import matplotlib


def f(x):
    return np.sin(x / 5.0) * np.exp(x / 10.0) + 5 * np.exp(-x / 2)


def create_matrix(left, right, step, degree):
    x = range(left, right, step)
    s = []
    y = []
    for p in x:
        y.append(f(p))
        s.append([float(p)**i for i in range(degree+1)])
    b = np.array(y)
    A = np.matrix(s)
    print A, b

if __name__ == "__main__":
    create_matrix(1, 16, 2, 1)


# Local minimum

import scipy
import scipy.optimize
import numpy as np

import funcs

BOUNDS = [1, 30]

if __name__ == "__main__":
    # with open('submission-1.txt', 'w') as answer:
    #     first = scipy.optimize.minimize(funcs.f, np.array([2.0]), method='BFGS')
    #     print first.x, first.fun
    #     answer.write(str(round(first.fun, 2)) + ' ')
    #     second = scipy.optimize.minimize(funcs.f, np.array([30.0]), method='BFGS')
    #     print second
    #     answer.write(str(round(second.fun, 2)))
    #     funcs.plot_func(funcs.f, BOUNDS)
    # with open('submission-2.txt', 'w') as s_answer:
    #     global_min = scipy.optimize.differential_evolution(funcs.f, bounds=[BOUNDS])
    #     print global_min
    #     s_answer.write(str(round(global_min.fun, 2)))
    with open('submission-3.txt', 'w') as t_answer:
        first = scipy.optimize.minimize(funcs.int_f, np.array([30.0]), method='BFGS')
        second = scipy.optimize.differential_evolution(funcs.int_f, bounds=[BOUNDS])
        print first
        print second
        t_answer.write(str(int(first.fun)) + ' ')
        t_answer.write(str(int(second.fun)))
        funcs.plot_func(funcs.int_f, BOUNDS)




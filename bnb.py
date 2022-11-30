import numpy as np
import data


def simplex(X, Y, Z):
    pass


def init():
    n = 3
    m = 4
    t = 5
    L, R, D, Q, A, P, S, M, C0, l0 = data.generate(n, m, t)
    c = np.hstack((-R, (S - P), -D))
    c = -c.T  # maximisation problem
    # ax <= b
    I_nm = np.identity(n * m, dtype="float")
    I_mt = np.identity(m * t, dtype="float")

    a = np.empty((0, n * m + m * t + n * m))
    # 3.1
    a1 = np.hstack(((-1 / l0) * I_nm, np.zeros((n * m, m * t)), I_nm))
    a = np.vstack((a, a1))

    # 3.2
    a1 = np.hstack(((1 / l0) * I_nm, np.zeros((n * m, m * t)), -I_nm))
    a = np.vstack((a, a1))

    # 4
    arrays = [np.identity(n) for _ in range(m)]
    new_arr = np.stack(arrays, axis=0).swapaxes(0, 2).reshape(n, n * m)

    a1 = np.hstack((new_arr, np.zeros((n, m * t + n * m))))

    a = np.vstack((a, a1))
    print(a.shape, a1.shape)

    # 5
    a1 = np.hstack((np.zeros((m * t, m * n)), I_mt, np.zeros((m * t, m * n))))
    a = np.vstack((a, a1))

    # 6
    arrays = [np.identity(m) for _ in range(t)]
    new_arr = -np.stack(arrays, axis=0).swapaxes(0, 1).reshape(m, m * t)

    a1 = np.hstack((np.zeros((m , m * n)), new_arr, np.zeros((m , m * n))))

    a = np.vstack((a, a1))

    # 7
    arrays = [np.identity(n) for _ in range(m)]
    a = np.stack(arrays, axis=0)
    new_arr = a.swapaxes(0, 1).reshape(n, n * m)

    arrays = [A[i] * np.identity(m) for i in range(t)]
    a = np.stack(arrays, axis=0)
    new_arr1 = a.swapaxes(0, 2).reshape(m, t * m)

    a1 = np.hstack((-new_arr, new_arr1, np.zeros((m * t, m * n))))
    a = np.vstack((a, a1))

    constraints = []

init()
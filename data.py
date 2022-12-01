import math

import numpy as np
from numpy import random


def generate(n, m, t):  # n milkmen, m factories, t items
    L = random.randint(500, 1000, size=(n))  # amount in litre
    R = random.randint(40, 45, size=(n))  # cost per litre in INR
    milkmen = random.randint(0, 200, size=(n, 2))  # coordinates of milkmen
    factories = random.randint(0, 200, size=(m, 2))  # coordinates of factories
    D = np.zeros((n, m))  # distance in kilometre, colunm of n columns of size m
    for i in range(n):
        for j in range(m):
            D[i][j] = math.dist(milkmen[i], factories[j])
    D = D.reshape(n * m)
    Q = random.randint(
        100, 10000, size=(m * t)
    )  # quantity of items, column m columns of size t
    A = random.uniform(0.1, 10, size=(t))  # amount per item in litre
    P = random.randint(1, 10, size=(t))  # production cost per item in INR
    S = random.randint(5, 500, size=(t))  # selling price per item in INR
    M = random.randint(1000, 50000, size=(t))  # minimum quantity per item
    C0 = 200
    l0 = 500
    return L, R, D, Q, A, P, S, M, C0, l0


def slackify(A, b, c):
    A = np.hstack((A, np.identity(A.shape[0])))
    c = np.append(c, np.zeros(A.shape[0]))
    return A, b, c


def init(n, m, t):
    # maximisation problem
    # max cTx
    # sub to. ax <= b
    # x>=0

    L, R, D, Q, A, P, S, M, C0, l0 = generate(n, m, t)

    arrays = [R for _ in range(m)]
    Rc = np.stack(arrays, axis=1).reshape(n * m)

    arrays = [S for _ in range(m)]
    Sc = np.stack(arrays, axis=0).reshape(m * t)

    arrays = [P for _ in range(m)]
    Pc = np.stack(arrays, axis=0).reshape(m * t)

    c = np.concatenate((-Rc, Sc - Pc, -C0 * D))
    I_nm = np.identity(n * m, dtype="float")
    I_mt = np.identity(m * t, dtype="float")

    a = np.empty((0, n * m + m * t + n * m))
    b = np.empty((0,))

    # 3.1
    a1 = np.hstack(((-1 / l0) * I_nm, np.zeros((n * m, m * t)), I_nm))
    a = np.vstack((a, a1))
    b = np.append(b, np.ones((n * m)))

    # 3.2
    a1 = np.hstack(((1 / l0) * I_nm, np.zeros((n * m, m * t)), -I_nm))
    a = np.vstack((a, a1))
    b = np.append(b, np.zeros((n * m)))

    # 4
    arrays = [np.identity(n) for _ in range(m)]
    new_arr = np.stack(arrays, axis=0).swapaxes(0, 2).reshape(n, n * m)

    a1 = np.hstack((new_arr, np.zeros((n, m * t + n * m))))
    a = np.vstack((a, a1))
    b = np.append(b, L)

    # 5
    a1 = np.hstack((np.zeros((m * t, m * n)), I_mt, np.zeros((m * t, m * n))))
    a = np.vstack((a, a1))
    b = np.append(b, Q)

    # 6
    arrays = [np.identity(t) for _ in range(m)]
    new_arr = -np.stack(arrays, axis=0).swapaxes(0, 1).reshape(t, m * t)

    a1 = np.hstack((np.zeros((t, m * n)), new_arr, np.zeros((t, m * n))))
    a = np.vstack((a, a1))
    b = np.append(b, -M)

    # 7
    arrays = [np.identity(m) for _ in range(n)]
    new_arr = -np.stack(arrays, axis=0).swapaxes(0, 1).reshape(m, n * m)

    arrays = [A[i] * np.identity(m) for i in range(t)]
    new_arr1 = np.stack(arrays, axis=0).swapaxes(0, 2).reshape(m, t * m)

    a1 = np.hstack((new_arr, new_arr1, np.zeros((m, m * n))))
    a = np.vstack((a, a1))
    b = np.append(b, np.zeros((m)))

    # size check
    assert a.shape == (b.size, c.size)

    return slackify(a, b, c)


def unflatten(sol, n, m, t):
    flat_x = sol[: n * m]
    flat_y = sol[n * m : n * m + m * t]
    flat_z = sol[n * m + m * t : 2 * n * m + m * t]

    x = flat_x.reshape(n, m)
    y = flat_y.reshape(m, t)
    z = flat_z.reshape(n, m)

    return x, y, z

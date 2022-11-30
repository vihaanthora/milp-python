import numpy as np
import data

def simplex(X, Y, Z):
    pass

def init():
    n = 3
    m = 4
    t = 5
    L, R, D, Q, A, P, S, M, C0, l0 = data.generate(n, m, t)
    c = np.hstack((-R, (S-P), -D))
    c = -c.T # maximisation problem
    # ax <= b
    Inm = np.identity(n*m, dtype="float")
    Imt = np.identity(m*t, dtype="float")

    a = np.array([[]])
    # 3.1
    a1 = np.hstack(((-1/l0)*Inm, (0)*Imt, Inm))
    a = np.append(a, a1, axis=0)

    # 3.2
    a1 = np.hstack(((1/l0)*Inm, (0)*Imt, -Inm))
    a = np.append(a, a1, axis=0)

    # 4
    arrays = [np.identity(n) for _ in range(m)]
    a = np.stack(arrays, axis=0)
    new_arr = a.swapaxes(0,2).reshape(n,n*m)

    a1 = np.hstack((new_arr, 0*Imt, 0*Inm))
    a = np.append(a, a1, axis=0)

    # 5
    a1 = np.hstack((0*Inm, Imt, 0*Inm))
    a = np.append(a, a1, axis=0)
    
    # 6
    arrays = [np.identity(m) for _ in range(t)]
    a = np.stack(arrays, axis=0)
    new_arr = a.swapaxes(0,1).reshape(m,m*t)

    a1 = np.hstack((0*Inm, -new_arr, 0*Inm))
    a = np.append(a, a1, axis=0)

    # 7
    arrays = [np.identity(n) for _ in range(m)]
    a = np.stack(arrays, axis=0)
    new_arr = a.swapaxes(0,1).reshape(n,n*m)

    arrays = [A[i]*np.identity(m) for i in range(t)]
    a = np.stack(arrays, axis=0)
    new_arr1 = a.swapaxes(0, 2).reshape(m, t * m)

    a1 = np.hstack((-new_arr, new_arr1, 0*Inm))
    a = np.append(a, a1, axis=0)

    constraints = []
    
init()
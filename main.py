from simplex import Simplex
from data import init, unflatten

n, m, t = 1, 2, 3
A, b, c = init(n, m, t)

solver = Simplex(A, b, c)

solution = solver.run()

X, Y, Z = unflatten(solution)

# print(X, Y, Z)
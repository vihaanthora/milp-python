from simplex import Simplex
from data import init, unflatten

n, m, t = 3, 3, 3
A, b, c = init(n, m, t)

solver = Simplex(A, b, c)

solution = solver.run()
# print(solution)
X, Y, Z = unflatten(solution, n, m, t)

print(f"X is \n {X}\n Y is \n {Y}\n Z is \n {Z}")

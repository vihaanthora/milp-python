from simplex import Simplex
from data import init, unflatten
from simplex1 import LinearModel
import numpy as np

n, m, t = 3, 3, 3
A, b, c = init(n, m, t)

print("A =\n", A, "\n")
print("b =\n", b, "\n")
print("c =\n", c, "\n\n")

solution = Simplex(A, b, -c).run()
print(f"Simplex {np.dot(solution, c)}")
X, Y, Z = unflatten(solution, n, m, t)
print(f"X is \n {X}\n Y is \n {Y}\n Z is \n {Z}")

#-----------------------------------------------------

model1 = LinearModel()

model1.addA(A)
model1.addB(b)
model1.addC(c)

solution = model1.optimize()
print(f"Simplex1 {np.dot(solution, c)}")
X, Y, Z = unflatten(solution, n, m, t)
print(f"X is \n {X}\n Y is \n {Y}\n Z is \n {Z}")
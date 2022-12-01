from simplex import Simplex
from data import init, unflatten, import_constraints
from tableu_simplex import LinearModel
from operator import itemgetter
import numpy as np

consts = import_constraints("dump.json")
n, m, t = itemgetter("n", "m", "t")(consts)
A, b, c = init(**consts)

model1 = Simplex(A, b, -c)
solution1, itermap1 = model1.run()
# X, Y, Z = unflatten(solution1, n, m, t)
print(f"Simplex1 {np.dot(solution1, c)}")
# print(f"X is \n {X}\n Y is \n {Y}\n Z is \n {Z}")
# print("Iterations:", itermap1)

# -----------------------------------------------------

model2 = LinearModel(A=A, b=b, c=c, minmax="MAX")
solution2, itermap2 = model2.optimize()
# X, Y, Z = unflatten(solution2, n, m, t)
print(f"Simplex2 {np.dot(solution2, c)}")
# print(f"X is \n {X}\n Y is \n {Y}\n Z is \n {Z}")
# print("Iterations:", itermap2)

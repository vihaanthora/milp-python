from data import *
from simplex import Simplex

INFILE_PATH = "data/inp4.json"
n, m, t = 100, 20, 25
LIMIT = 50000
profit = 0
iter = 0
allPos = False

while profit < LIMIT and not allPos:
    consts = generate(n, m, t)
    A, b, c = LP_form(n, m, t, *consts)
    model1 = Simplex(A, b, -c)
    solution1, itermap1 = model1.run()
    allPos = (solution1 >= 0).all()
    profit = np.dot(solution1, c)
    iter += 1
    if iter % 100 == 0:
        print("Iteration:", iter)

print(iter)
export_constraints(INFILE_PATH, n, m, t, *consts)
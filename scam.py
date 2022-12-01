from data import *
from simplex import Simplex

n, m, t = 3, 10, 5
LIMIT = 50000
profit = 0
iter = 0
allPos = False

while profit < LIMIT and not allPos:
    consts = generate(n, m, t)
    A, b, c = init(n, m, t, *consts)
    model1 = Simplex(A, b, -c)
    solution1, itermap1 = model1.run()
    allPos = (solution1 >= 0).all()
    profit = np.dot(solution1, c)
    iter += 1
    if iter % 100 == 0:
        print("Iteration:", iter)

print(iter)
export_constraints(n, m, t, *consts, "dump.json")

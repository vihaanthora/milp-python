from simplex import Simplex
from tableu_simplex import LinearModel
from timeit import default_timer as timer

def solve(A, b, c, method=1):
    if method == 1:
        model = Simplex(A, b, -c)
        start = timer()
        solution, itermap = model.run()
        time = timer() - start
    elif method == 2:
        model = LinearModel(A, b, c, minmax="MAX")
        start = timer()
        solution, itermap = model.optimize()
        time = timer() - start
    else:
        print("No such method available")
        exit(1)

    return solution, itermap, time

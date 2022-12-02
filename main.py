from operator import itemgetter
from data import (
    LP_form,
    unflatten,
    import_constraints,
    export_results,
    processZ,
    calc_obj,
)
from wrapper import solve

INFILE_PATH = "data/inp4.json"
OUTFILE_PATH = "data/out4.json"

consts = import_constraints(INFILE_PATH)
A, b, c = LP_form(**consts)

solution, itermap, time = solve(A, b, c, method=1)

n, m, t, D = itemgetter("n", "m", "t", "D")(consts)
solution = processZ(solution, D, n, m, t)
X, Y, Z = unflatten(solution, n, m, t)
objf = calc_obj(solution, c)
iter = max(itermap.keys())



export_results(OUTFILE_PATH, X, Y, Z, iter, objf, 1)
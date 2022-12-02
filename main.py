import argparse
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

parser = argparse.ArgumentParser(prog="MILP Python", description="Solve MILPs")
parser.add_argument(
    "-m",
    metavar="method",
    dest="method",
    choices=(1, 2),
    type=int,
    default=1,
    help="1. Matrix Simplex Method\n2. Tableau Simplex Method",
)
parser.add_argument(
    "-i",
    metavar="input",
    dest="input",
    type=str,
    default="data/inp1.json",
    help="Input file path",
)
parser.add_argument(
    "-o",
    metavar="output",
    dest="output",
    type=str,
    default="data/out.json",
    help="Output file path",
)
args = parser.parse_args()


INFILE_PATH = args.input
OUTFILE_PATH = args.output
METHOD = args.method

consts = import_constraints(INFILE_PATH)
A, b, c = LP_form(**consts)

solution, itermap, time = solve(A, b, c, method=METHOD)

n, m, t, D = itemgetter("n", "m", "t", "D")(consts)
solution = processZ(solution, D, n, m, t)
X, Y, Z = unflatten(solution, n, m, t)
objf = calc_obj(solution, c)
iter = max(itermap.keys())



export_results(OUTFILE_PATH, X, Y, Z, iter, objf, 1)
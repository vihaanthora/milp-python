import argparse
from data import *

parser = argparse.ArgumentParser(prog="MILP Python", description="Solve MILPs")
parser.add_argument("-n", metavar="n", dest="n", type=int, required=True)
parser.add_argument("-m", metavar="m", dest="m", type=int, required=True)
parser.add_argument("-t", metavar="t", dest="t", type=int, required=True)
parser.add_argument(
    "-o",
    metavar="output",
    dest="output",
    type=str,
    default="data/out.json",
    help="Output file path",
)

args = parser.parse_args()

OUTFILE_PATH = args.output
n, m, t = args.n, args.m, args.t
consts = generate(n, m, t)

export_constraints(OUTFILE_PATH, n, m, t, *consts)

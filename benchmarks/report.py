from argparse import ArgumentParser
import uniform_primitive
import weighted_primitive
from benchmark import report_benchmark

parser = ArgumentParser()
parser.add_argument('-l', '--levels', type=int, default=5, help="Number of sampled elements.")
parser.add_argument('--runs', type=int, default=1000, help="Number of runs for each sampling statement.")
parser.add_argument('--repeat', type=int, default=3, help="Repeats for benchmarks and average.")
parser.add_argument('-b', '--benchmark', type=str, default='uniform_primitive', choices=['uniform_primitive', 'weighted_primitive'])

args = parser.parse_args()

if args.benchmark == 'uniform_primitive':
    benchmark = uniform_primitive.benchmarks
elif args.benchmark == 'weighted_primitive':
    benchmark = weighted_primitive.benchmarks
    
num_elems = [10**i for i in range(1, args.levels + 1)]

print(f"Running benchmark {args.benchmark}")
t = report_benchmark(benchmark, num_elems, args.runs, args.repeat)
print(t)

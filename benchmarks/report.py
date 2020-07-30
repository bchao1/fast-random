import uniform_primitive
import weighted_primitive
from benchmark import report_benchmark

num_elems = [10**i for i in range(1, 6)]
runs = 1000
repeat = 3

t = report_benchmark(weighted_primitive.benchmarks, num_elems, runs, repeat)

print(t)
import timeit
import numpy as np
from tabulate import tabulate

class Benchmark(object):
    def __init__(self, name, stmt, setup):
        self._name = name
        self._stmt = stmt
        self._setup = setup
        self._n = 10
    
    @property
    def name(self):
        return self._name
    
    @property
    def stmt(self):
        return self._stmt
    
    @property
    def setup(self):
        return self._setup.format(self._n)
    
    def set_num(self, n):
        self._n = n
    

def report_benchmark(benchmarks, num_elems, runs, repeat):

    table = []
    for n in num_elems:
        print(f"Benchmarking {n} elements ...")
        for b in benchmarks:
            b.set_num(n)
        res = [np.mean(timeit.repeat(
            stmt=b.stmt, setup=b.setup, number=runs, repeat=repeat)) for b in benchmarks]
        table.append(res)

    table = np.transpose(np.array(table))

    headers = [''] + num_elems
    table = [[benchmarks[i].name] + list(res) for i, res in enumerate(table) ]
    return tabulate(table, headers = headers)
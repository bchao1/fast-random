from benchmark import Benchmark

benchmarks = []

benchmarks.append(Benchmark(
    name = 'random.choices weighted (list)',
    setup = 'from random import choices; import numpy as np; elems=[0]*{}; weights=np.random.random(len(elems));',
    stmt = "_ = choices(population=elems, weights=weights)"
))

benchmarks.append(Benchmark(
    name = 'random.choice weighted (np.array)',
    setup = 'from random import choices; import numpy as np; elems=np.zeros({}); weights=np.random.random(len(elems));',
    stmt = "_ = choices(population=elems, weights=weights)"
))

benchmarks.append(Benchmark(
    name = 'np.random.choice weighted (np.array)',
    setup = 'from numpy.random import choice; import numpy as np; elems=[0]*{}; p = np.random.random(len(elems)); p /= np.sum(p); ',
    stmt = "_ = choice(elems, p=p)"
))

benchmarks.append(Benchmark(
    name = 'np.random.choice weighted(int)',
    setup = 'from numpy.random import choice; import numpy as np; n={}; p = np.random.random(n); p /= np.sum(p); ',
    stmt = "_ = choice(n, p=p)"
))
    
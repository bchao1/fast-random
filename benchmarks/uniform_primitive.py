from benchmark import Benchmark

benchmarks = []

benchmarks.append(Benchmark(
    name = 'random.choice (list)',
    setup = 'from random import choice; elems=[0]*{};',
    stmt = "_ = choice(elems)"
))

benchmarks.append(Benchmark(
    name = 'random.choice (np.array)',
    setup = 'from random import choice; import numpy as np; elems=np.zeros({});',
    stmt = "_ = choice(elems)"
))

benchmarks.append(Benchmark(
    name = 'np.random.choice (list)',
    setup = 'from numpy.random import choice; import numpy as np; elems=[0]*{};',
    stmt = "_ = choice(elems)"
))

benchmarks.append(Benchmark(
    name = 'np.random.choice (array)',
    setup = 'import numpy as np; from numpy.random import choice; import numpy as np; elems=np.zeros({});',
    stmt = "_ = choice(elems)"
))

benchmarks.append(Benchmark(
    name = 'np.random.choice (int)',
    setup = 'from numpy.random import choice; n={};',
    stmt = "_ = choice(n)"
))
    
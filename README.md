# fast-random
> Fast wrapper for `random.choice` and `numpy.random.choice`. Also benchmarking.

## Tests
- Sample from a list of primitives uniformly (not specifying `p` or `weights`)
- Sample from a list of primitive with weights / probability distribution (specifying `p` or `weights` parameters)
- Sample from a list of objects

## Benchmarks
### Uniformly sampling primitives
||10|100|1000|10000|100000|
|--|--|--|--|--|--|
|random.choice (list)      |0.000725666  |0.000659164  |0.000879995  |0.000753662  |0.000730284|
|random.choice (np.array)  |0.000768288  |0.000738777  |0.00129219   |0.00108727   |0.000902|
|np.random.choice (list)   |0.0050106    |0.0119155    |0.0817819    |0.625917     |6.33594|
|np.random.choice (array)  |0.00187023   |0.00280155   |0.00169472   |0.00163102   |0.00161765|
|np.random.choice (int)    |0.0035767    |0.00200371   |0.0020327    |0.00202595   |0.00206575|

### Weighted sampling primitives

|                                     |         10 |       100 |      1000 |    10000 |  100000|
|------------------------------------ | ---------- | --------- | --------- | -------- |--------|
|random.choices weighted (list)       | 0.00750973 | 0.0157622 | 0.096552  | 0.912059 | 9.39231|
|random.choice weighted (np.array)    | 0.00430348 | 0.012958  | 0.0980954 | 0.901568 | 9.25725|
|np.random.choice weighted (np.array) | 0.0221554  | 0.0277225 | 0.0939044 | 0.732089 | 7.30494|
|np.random.choice weighted(int)       | 0.0192122  | 0.0201531 | 0.0287501 | 0.103373 | 0.8215|

## Running benchmarks 
Plese check `benchmarks/report.py`.

## Takeaways

## Reference
[Discussion on StackOverflow](https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice)
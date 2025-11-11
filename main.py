from google_examples import BinPackingSimple

problem = BinPackingSimple([4, 8, 1, 4, 2, 1, 3, 5, 7, 3], bin_capacity=10)
#[48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30]
problem.run_solve(show_IDs=False)

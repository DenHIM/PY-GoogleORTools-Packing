from google_examples import BinPackingSimple, BinPackingMultiBin, BinPackingCost

data = [4, 7, 1, 4, 2, 1, 3, 5, 7, 3]

#problem = BinPackingSimple([4, 7, 1, 4, 2, 1, 3, 5, 7, 3], bin_capacity=10)
#problem.run_solve(show_IDs=False)
#problem = BinPackingSimple([48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30], bin_capacity=100)
#problem.run_solve(show_IDs=False)
#problem = BinPackingMultiBin([7, 3, 3, 3, 10], bin_capacities=[7, 10])
#problem.run_solve(show_IDs=False)
#problem = BinPackingMultiBin([4, 7, 1, 4, 2, 1, 3, 5, 7, 3], bin_capacities=[7,10])
#problem.run_solve(show_IDs=False)
problem = BinPackingSimple(data, bin_capacity=10)
problem.run_solve(show_IDs=False)
problem = BinPackingMultiBin(data, bin_capacities=[7, 10])
problem.run_solve(show_IDs=False)
problem = BinPackingCost(data, bin_capacities=[7,10], bin_costs=[2,4])
problem.run_solve(show_IDs=False)

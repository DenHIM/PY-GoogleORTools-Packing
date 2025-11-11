#import numpy as np
from ortools.linear_solver import pywraplp

class BinPackingSimple:
    data = {}

    def __init__(self, weights, bin_capacity=100):
        self.init_data_model(weights, bin_capacity)

    def init_data_model(self, weights, bin_capacity):
        """Create the data for the example."""
        self.data["weights"] = weights
        self.data["items"] = list(range(len(weights)))
        self.data["bins"] = self.data["items"]
        self.data["bin_capacity"] = bin_capacity

    def run_solve(self, show_IDs=True):
        solver = pywraplp.Solver.CreateSolver('SCIP')
        if not solver:
            return

        # Variables
        # x[i, j] = 1 if item i is packed in bin j.
        x = {}
        for i in self.data["items"]:
            for j in self.data["bins"]:
                x[(i, j)] = solver.IntVar(0, 1, "x_%i_%i" % (i, j))

        # y[j] = 1 if bin j is used.
        y = {}
        for j in self.data["bins"]:
            y[j] = solver.IntVar(0, 1, "y[%i]" % j)
            
        # Constraints
        # Each item must be in exactly one bin.
        for i in self.data["items"]:
            solver.Add(sum(x[i, j] for j in self.data["bins"]) == 1)

        # The amount packed in each bin cannot exceed its capacity.
        for j in self.data["bins"]:
            solver.Add(
                sum(x[(i, j)] * self.data["weights"][i] for i in self.data["items"])
                <= y[j] * self.data["bin_capacity"]
            )

        # Objective: minimize the number of bins used.
        solver.Minimize(solver.Sum([y[j] for j in self.data["bins"]]))

        # Solving the problem.
        print(f"Solving with {solver.SolverVersion()}")
        status = solver.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            num_bins = 0
            for j in self.data["bins"]:
                if y[j].solution_value() == 1:
                    bin_items = []
                    bin_items_weight = []
                    bin_weight = 0
                    for i in self.data["items"]:
                        if x[i, j].solution_value() > 0:
                            bin_items.append(i)
                            bin_items_weight.append(self.data["weights"][i])
                            bin_weight += self.data["weights"][i]
                    if bin_items:
                        num_bins += 1
                        print("Bin number", j)
                        if show_IDs:
                            print("  Items packed (IDs):", bin_items)
                        print("  Items packed (Weight):", bin_items_weight)
                        print("  Total weight:", bin_weight)
                        print()
            print()
            print("Number of bins used:", num_bins)
            print("Time = ", solver.WallTime(), " milliseconds")
        else:
            print("The problem does not have an optimal solution.")


class BinPackingMultiBin:
    data = {}

    def __init__(self, weights, bin_capacities=[100]):
        self.init_data_model(weights, bin_capacities)

    def init_data_model(self, weights, bin_capacities):
        """Create the data for the example."""
        self.data["weights"] = weights
        self.data["items"] = list(range(len(weights)))
        self.data["bins"] = []
        for bin_cap in bin_capacities:
            self.data["bins"] += [bin_cap for _ in self.data["items"]]

    def run_solve(self, show_IDs=True):
        solver = pywraplp.Solver.CreateSolver('SCIP')
        if not solver:
            return

        # Variables
        # x[i, j] = 1 if item i is packed in bin j.
        x = {}
        for i in self.data["items"]:
            for j, _ in enumerate(self.data["bins"]):
                x[(i, j)] = solver.IntVar(0, 1, "x_%i_%i" % (i, j))

        # y[j] = 1 if bin j is used.
        y = {}
        for j, _ in enumerate(self.data["bins"]):
            y[j] = solver.IntVar(0, 1, "y[%i]" % j)
            
        # Constraints
        # Each item must be in exactly one bin.
        for i in self.data["items"]:
            solver.Add(sum(x[i, j] for j, _ in enumerate(self.data["bins"])) == 1)

        # The amount packed in each bin cannot exceed its capacity.
        for j, bin_cap in enumerate(self.data["bins"]):
            solver.Add(
                sum(x[(i, j)] * self.data["weights"][i] for i in self.data["items"])
                <= y[j] * bin_cap
            )

        # Objective: minimize the number of bins used.
        solver.Minimize(solver.Sum([y[j] for j, _ in enumerate(self.data["bins"])]))

        # Solving the problem.
        print(f"Solving with {solver.SolverVersion()}")
        status = solver.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            num_bins = 0
            for j, _ in enumerate(self.data["bins"]):
                if y[j].solution_value() == 1:
                    bin_items = []
                    bin_items_weight = []
                    bin_weight = 0
                    for i in self.data["items"]:
                        if x[i, j].solution_value() > 0:
                            bin_items.append(i)
                            bin_items_weight.append(self.data["weights"][i])
                            bin_weight += self.data["weights"][i]
                    if bin_items:
                        num_bins += 1
                        print("Bin number", j)
                        if show_IDs:
                            print("  Items packed (IDs):", bin_items)
                        print("  Items packed (Weight):", bin_items_weight)
                        print("  Total weight:", bin_weight)
                        print()
            print()
            print("Number of bins used:", num_bins)
            print("Time = ", solver.WallTime(), " milliseconds")
        else:
            print("The problem does not have an optimal solution.")
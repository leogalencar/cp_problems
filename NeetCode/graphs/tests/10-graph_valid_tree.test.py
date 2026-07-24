import importlib
import os
import sys

# Add the root directory 'cp_problems' to the Python path
# This allows us to import 'solver' from anywhere in the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from solver import run_tests

# Dynamically import the solution file.
# We use importlib because the file name starts with a number and has dashes,
# which makes it an invalid Python identifier for standard 'import' syntax.
solution_module = importlib.import_module("10-graph_valid_tree")
validTree = solution_module.Solution().validTree

test_cases = [
    {"inputs": [5, [[0, 1], [0, 2], [0, 3], [1, 4]]], "expected": True},
    {"inputs": [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]], "expected": False},
    {"inputs": [1, [[0, 0]]], "expected": False},
]

if __name__ == "__main__":
    run_tests(
        func=validTree,
        test_cases=test_cases,
        time_limit=1.0,
        check_type=True,
        disallow_original_input_return=False,
    )

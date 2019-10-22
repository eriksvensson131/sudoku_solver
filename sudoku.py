import sudoku_puzzles
import SudokuSolver
import numpy as np
import sys
sys.setrecursionlimit(20000)


puzzle = np.array(sudoku_puzzles.puzzle2)

print(f'The original puzzle looks like:\n{puzzle}')

ss = SudokuSolver.SudokuSolver(puzzle)

print(ss.solve(0, 1))

#print(ss.puzzle)
#print('where are we?')
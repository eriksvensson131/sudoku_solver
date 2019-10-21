import numpy as np
import sudoku_puzzles
from collections import namedtuple
import sys
sys.setrecursionlimit(20000)

Pos = namedtuple('Pos', 'row col')
counter = 0

puzzle = np.array(sudoku_puzzles.puzzle2)
print(f'The original puzzle looks like:\n{puzzle}')

def check_number(puzzle, pos, n):
	if ( 
		(n in puzzle[slice_row(pos)]) or
		(n in puzzle[slice_col(pos)]) or
		(n in puzzle[slice_square(pos)])
	   ):
		return False
	else:
		return True

def slice_row(pos):
	return np.s_[pos.row, :]

def slice_col(pos):
	return np.s_[:,pos.col]

def slice_square(pos):
	square_x = pos.row // 3
	square_y = pos.col // 3
	return np.s_[square_x*3:square_x*3+3, square_y*3:square_y*3+3]

unsolved = [Pos(row, col) for row in range(9)
						  for col in range(9)
						  if puzzle[row, col] == 0]

def solve(puzzle, i, n):
	if i < len(unsolved): 
		pos = unsolved[i]
		if n == 10:
			puzzle[pos] = 0
			solve(puzzle, i-1, puzzle[unsolved[i-1]] + 1)
		else: 
			if check_number(puzzle, pos, n):
				puzzle[pos] = n
				solve(puzzle, i+1, 1)
			else:
				solve(puzzle, i, n+1)
	else:
		print(puzzle)
		print('puzzle solved')

solve(puzzle, 0, 1)

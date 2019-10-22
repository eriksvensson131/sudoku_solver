#Importing from standard libraries
from collections import namedtuple

#Import third party libraries
import numpy as np

Pos = namedtuple('Pos', 'row col')

class SudokuSolver:

	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.unsolved = [Pos(row, col) for row in range(9)
									   for col in range(9)
									   if puzzle[row, col] == 0]

	def check_number(self, pos, n):
		if ( 
			(n in self.puzzle[self.slice_row(pos)]) or
			(n in self.puzzle[self.slice_col(pos)]) or
			(n in self.puzzle[self.slice_square(pos)])
		   ):
			return False
		else:
			return True

	def slice_row(self, pos):
		return np.s_[pos.row, :]

	def slice_col(self, pos):
		return np.s_[:,pos.col]

	def slice_square(self, pos):
		square_x = pos.row // 3
		square_y = pos.col // 3
		return np.s_[square_x*3:square_x*3+3, square_y*3:square_y*3+3]

	def solve(self, i, n):
		if i < 0:
			return 'no possible solution'
		elif i == len(self.unsolved):
			print(self.puzzle)
			return 'puzzle solved'
		else:
			pos = self.unsolved[i]
			if n == 10:
				self.puzzle[pos] = 0
				i -= 1
				n = self.puzzle[self.unsolved[i]] + 1
				return self.solve(i, n)
			else: 
				if self.check_number(pos, n):
					self.puzzle[pos] = n
					return self.solve(i+1, 1)
				else:
					return self.solve(i, n+1)
			


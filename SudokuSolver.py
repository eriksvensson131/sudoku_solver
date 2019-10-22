#Importing from standard libraries
from collections import namedtuple

#Importing from third party libraries
import numpy as np

Pos = namedtuple('Pos', 'row col')

class SudokuSolver:

	def __init__(self, board):
		self.board = board

	def check_number(self, board, pos, n):
		if ( 
			(n in board[self.slice_row(pos)]) or
			(n in board[self.slice_col(pos)]) or
			(n in board[self.slice_square(pos)])
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

	def find_empty(self, board):
	    for i in range(len(board)):
	        for j in range(len(board[i])):
	            if board[i][j] == 0:
	                return i,j
	    else:
	        return False

	def solve(self, board):
		empty_space = self.find_empty(board)
		if not empty_space:
			print(board)
			return True
		else:
			pos = Pos(*empty_space)

		for n in range(1,10):
			if self.check_number(board, pos, n):
				board[pos] = n
				if self.solve(board):
					return True
				board[pos] = 0
		else:
			return False


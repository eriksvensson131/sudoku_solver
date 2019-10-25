# Importing from standard libraries
from collections import namedtuple
Pos = namedtuple('Pos', 'row col')

# Importing from third party libraries
import numpy as np

class SudokuSolver:
    """Solves sudokus"""
    def __init__(self, board):
        self.board = np.array(board)
        self.solutions = []
        self.numberOfSolutions = 0

    @staticmethod
    def check_number(board, pos, n):
        """Checks if number n is valid in position pos in the given board"""
        rowSlice = np.s_[pos.row, :]
        columnSlice = np.s_[:, pos.col]
        square_x = pos.row // 3
        square_y = pos.col // 3
        squareSlice = np.s_[square_x * 3:square_x * 3 + 3, square_y * 3:square_y * 3 + 3]
        if ((n in board[rowSlice]) or
            (n in board[columnSlice]) or
            (n in board[squareSlice])):
            return False
        else:
            return True

    @staticmethod
    def find_empty(board):
        """find next empty space on the board, parses the board from top left"""
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    return Pos(i, j)
        return None

    def solve(self, findAll=False):
        """starts the recursion"""
        self.recursive_solve(self.board.copy(), findAll)
        if self.solutions:
            print(f'The following {len(self.solutions)} solutions where found:\n')
            for i, board in enumerate(self.solutions, 1):
                print(f'#{i}\n{board} \n')

    def recursive_solve(self, board, findAll=False):
        """Solves the board recursively, updates the solvedBoard when finished.
           If findAll flag is set to true solvedBoard will be updated to a list with
           all solutions"""
        empty_space = self.find_empty(board)
        if not empty_space:
            self.solutions.append(board.copy())
            return not findAll #If True is returned only one solution is found
        else:
            pos = empty_space

        for n in range(1, 10):
            if self.check_number(board, pos, n):
                board[pos] = n
                if self.recursive_solve(board, findAll):
                    return True
                board[pos] = 0
        else:
            return False

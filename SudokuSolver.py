# Importing from standard libraries
from collections import namedtuple
import time

# Importing from third party libraries
import numpy as np

Pos = namedtuple('Pos', 'row col')


def clock(func):
    """Decorator which times the time it takes for functions"""
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        print(f'{elapsed:.2f}s to solve with \"{name}\"')
        return result
    return clocked


class Sudoku:
    """Creates or solves sudokus"""
    def __init__(self, board=None):
        self.board = self.set_board(board)
        self._empty_spaces = self.empty_spaces(board=self.board)
        self.solutions = []
        self.number_of_solutions = 0

    def set_board(self, board):
        """Sets the board, generates a random sudoku if board=None"""
        if board:
            return np.array(board)
        else:
            return self.generate_sudoku()

    @staticmethod
    def check_number(board, pos, n):
        """Checks if number n is valid in position pos in the given board"""
        row_slice = np.s_[pos.row, :]
        column_slice = np.s_[:, pos.col]
        square_x = pos.row // 3
        square_y = pos.col // 3
        square_slice = np.s_[square_x * 3:square_x * 3 + 3, square_y * 3:square_y * 3 + 3]
        if ((n in board[row_slice]) or
            (n in board[column_slice]) or
            (n in board[square_slice])):
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

    def find_empty2(self, board):
        """uses the _empty_spaces list to return an empty position with
        the lowest possible numbers"""
        for pos in self._empty_spaces:
            if board[pos] == 0:
                return pos
        else:
            return None

    @clock
    def solve(self, find_all=False):
        """starts the recursion"""
        self.solutions = []
        board = self.board.copy()
        self.recursive_solve(board, find_all)

    def show_board(self):
        """Prints the current board state"""
        print(self.board)

    def empty_spaces(self, board):
        """Returns a sorted list of the empty positions on the board. The list is sorted
        with the position having the fewest allowed possible numbers first"""
        counting_possible_numbers = []
        positions = [Pos(row, col) for row in range(9)
                                   for col in range(9)
                                   if board[row, col] == 0]
        for pos in positions:
            possible_numbers = 0
            for n in range(1, 10):
                if self.check_number(board, pos, n):
                    possible_numbers += 1
            counting_possible_numbers.append((pos, possible_numbers))
        counting_possible_numbers = sorted(counting_possible_numbers, key=lambda x: x[1])
        return [x[0] for x in counting_possible_numbers]

    def recursive_solve(self, board, find_all=False):
        """Solves the board recursively, updates the solvedBoard when finished.
           If find_all flag is set to true all possible solutions will be found"""
        empty_space = self.find_empty(board)
        if not empty_space:  # base case, a filled board
            self.solutions.append(board.copy())
            if len(self.solutions) >= 15:  # Abort recursion if more than 15 solutions are found
                return True
            return not find_all  # find_all = True will continue recursion and start backtracking
        else:
            pos = empty_space

        for n in range(1, 10):
            if self.check_number(board, pos, n):
                board[pos] = n
                if self.recursive_solve(board, find_all):
                    return True
                board[pos] = 0
        else:
            return False

    def generate_sudoku(self, initial_values=25):
        """A function to generate sudokus which is not fully implemented"""
        board = np.zeros([9, 9]).astype('int')
        set_values = 0
        while set_values <= initial_values:
            row = np.random.randint(0, 9)
            col = np.random.randint(0, 9)
            n = np.random.randint(1, 10)
            pos = Pos(row, col)
            if self.check_number(board, pos, n):
                board[pos] = n
                set_values += 1
        return board

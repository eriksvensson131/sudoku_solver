# Importing from standard libraries
from collections import namedtuple
Pos = namedtuple('Pos', 'row col')

# Importing from third party libraries
import numpy as np

class Sudoku:
    """Solves sudokus"""
    def __init__(self, board=None):
        self.board = self.set_board(board)
        self.solutions = []
        self.numberOfSolutions = 0

    def set_board(self, board):
        """Sets the board, generates a random sudoku if board=None"""
        if board:
            return np.array(board)
        else:
            return self.generate_sudoku()

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
        print('Initial board looks like this')
        print(self.board)
        board = self.solve_sure_numbers(self.board.copy())
        self.recursive_solve(board, findAll)
        if self.solutions:
            print(f'The following {len(self.solutions)} solutions where found:')
            for i, board in enumerate(self.solutions, 1):
                print(f'#{i}\n{board} \n')
        else:
            'no possible solutions for this puzzle'

    def show_board(self):
        """Prints the current board state"""
        print(self.board)

    def solve_sure_numbers(self, board):
        """Returns a board where sure numbers are added"""
        found_new = True
        sureNumbers = 0
        while found_new:
            positions = [Pos(row, col) for row in range(9)
                                       for col in range(9)
                                       if board[row, col] == 0]
            for pos in positions:
                possible_numbers = []
                for n in range(1, 10):
                    if self.check_number(board, pos, n):
                        possible_numbers.append(n)
                if len(possible_numbers) == 1:
                    board[pos] = possible_numbers[0]
                    sureNumbers +=1
                    found_new = True
            else:
                found_new = False
        print(f'{sureNumbers} sure numbers were found:')
        print(board)
        return board

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

    def generate_sudoku(self, initialValues=25):
        board = np.zeros([9, 9]).astype('int')
        setValues = 0
        while setValues <= initialValues:
            row = np.random.randint(0, 9)
            col = np.random.randint(0, 9)
            n = np.random.randint(1,10)
            pos = Pos(row, col)
            if self.check_number(board, pos, n):
                board[pos] = n
                setValues += 1
        return board

import sudokuPuzzles
import SudokuSolver
import argparse

def str2bool(s):
    if isinstance(s, bool):
        return s
    if s.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif s.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected')

parser = argparse.ArgumentParser(description='Solve a sudoku')
parser.add_argument('puzzleNumber', metavar='puzzle', type=str,
                    help='select puzzle number or generate')
parser.add_argument('findAll', metavar='boolean', type=str2bool, nargs='?',
                    default=False, help='look for more than one solution?')
args = parser.parse_args()

puzzles = sudokuPuzzles.puzzle_dict
findAll = args.findAll
puzzleNumber = args.puzzleNumber
if puzzleNumber == 'generate':
    sudoku = SudokuSolver.Sudoku(None)
    sudoku.show_board()
    sudoku.solve(findAll=False)
else:
    board = puzzles[puzzleNumber]
    sudoku = SudokuSolver.Sudoku(board)
    print(f'The original puzzle looks like:\n{sudoku.board}\n')
    sudoku.solve(findAll)




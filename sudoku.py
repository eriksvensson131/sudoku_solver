import sudoku_puzzles
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
                    help='select puzzle1, puzzle2, puzzle3 or puzzle4')
parser.add_argument('findAll', metavar='boolean', type=str2bool, nargs='?',
                    default=False, help='look for more than one solution?')
args = parser.parse_args()

puzzles = sudoku_puzzles.puzzle_dict
board = puzzles[args.puzzleNumber]
findAll = args.findAll

ss = SudokuSolver.SudokuSolver(board)

print(f'The original puzzle looks like:\n{ss.board}\n')
ss.solve(findAll)
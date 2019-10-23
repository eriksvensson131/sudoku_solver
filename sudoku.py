import sudoku_puzzles
import SudokuSolver
import argparse


parser = argparse.ArgumentParser(description='Solve a sudoku')
parser.add_argument('puzzleNumber', metavar='puzzle', type=str,
                    help='select puzzle1, puzzle2, puzzle3 or puzzle4')
args = parser.parse_args()

puzzles = sudoku_puzzles.puzzle_dict
board = puzzles[args.puzzleNumber]

ss = SudokuSolver.SudokuSolver(board)

print(f'The original puzzle looks like:\n{ss.board}\n')
ss.solve()


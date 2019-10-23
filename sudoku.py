import sudoku_puzzles
import SudokuSolver

puzzles = sudoku_puzzles.puzzle_dict
ss = SudokuSolver.SudokuSolver(puzzles['puzzle3'])

print(f'The original puzzle looks like:\n{ss.board}\n')
ss.solve()


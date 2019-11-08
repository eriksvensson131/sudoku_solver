import sudokuPuzzles
import SudokuSolver
import Argparser

argparser = Argparser.Argparser()
find_all = argparser.find_all
puzzle_number = argparser.puzzle_number

puzzles = sudokuPuzzles.puzzle_dict


def show_solutions(solutions):
    if solutions:
        print(f'The following {len(solutions)} solutions where found:')
        for i, board in enumerate(solutions, 1):
            print(f'#{i}\n{board} \n')
    else:
        print('no possible solutions for this puzzle')


if puzzle_number == 'generate':
    sudoku = SudokuSolver.Sudoku(None)
    sudoku.show_board()
    sudoku.solve(find_all)
    show_solutions(sudoku.solutions)
else:
    puzzle = puzzles[puzzle_number]
    sudoku = SudokuSolver.Sudoku(puzzle)
    print(f'The original puzzle looks like:\n{sudoku.board}\n')
    sudoku.solve(find_all)
    show_solutions(sudoku.solutions)






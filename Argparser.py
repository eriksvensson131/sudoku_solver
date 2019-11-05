import argparse


class Argparser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Solve a sudoku')
        self.parser.add_argument('puzzle_number', metavar='puzzle', type=str,
                            help='select puzzle number or generate, e.g. \'puzzle1\'')
        self.parser.add_argument('find_all', metavar='find_all', type=self.str2bool, nargs='?',
                            default=False, help='look for more than one solution? Y/N')
        self.args = self.parser.parse_args()
        self.find_all = self.args.find_all
        self.puzzle_number = self.args.puzzle_number

    @staticmethod
    def str2bool(s):
        if isinstance(s, bool):
            return s
        if s.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif s.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected')


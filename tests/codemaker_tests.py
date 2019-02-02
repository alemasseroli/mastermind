import unittest

from mastermind.board import Board
from mastermind.codemaker import Codemaker

HOLES = 4
COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PINK']


class CodemakerTests(unittest.TestCase):

    def test_create_code(self):
        board = Board(COLORS, HOLES)
        codemaker = Codemaker()
        codemaker.create_code(board)
        assert len(codemaker.code) == HOLES
        for color in codemaker.code:
            assert color in COLORS

    def test_evaluate_guess_empty(self):
        self.assert_evaluate_output(
            code=['RED', 'RED', 'RED', 'RED'],
            guess=['BLUE', 'BLUE', 'BLUE', 'BLUE'],
            expected=[]
        )

    def test_evaluate_guess_all_black(self):
        self.assert_evaluate_output(
            code=['RED', 'RED', 'RED', 'RED'],
            guess=['RED', 'RED', 'RED', 'RED'],
            expected=['BLACK', 'BLACK', 'BLACK', 'BLACK']
        )

    def test_evaluate_guess_all_white(self):
        self.assert_evaluate_output(
            code=['RED', 'BLUE', 'GREEN', 'YELLOW'],
            guess=['YELLOW', 'RED', 'BLUE', 'GREEN'],
            expected=['WHITE', 'WHITE', 'WHITE', 'WHITE']
        )

    def test_evaluate_with_disordered_guesses(self):
        self.assert_evaluate_output(
            code=['RED', 'RED', 'RED', 'BLUE'],
            guess=['RED', 'RED', 'BLUE', 'BLUE'],
            expected=['BLACK', 'BLACK', 'BLACK']
        )

    def test_evaluate_with_disordered_guesses_and_repetitions(self):
        self.assert_evaluate_output(
            code=['PINK', 'YELLOW', 'PINK', 'BLUE'],
            guess=['PINK', 'PINK', 'YELLOW', 'YELLOW'],
            expected=['BLACK', 'WHITE', 'WHITE']
        )

    def assert_evaluate_output(self, code, guess, expected):
        codemaker = Codemaker()
        codemaker.code = code
        output = codemaker.evaluate_guess(guess)
        assert expected == output


if __name__ == '__main__':
    unittest.main()

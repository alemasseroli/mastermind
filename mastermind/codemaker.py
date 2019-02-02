# coding=utf-8
import random


class Codemaker:
    code = None

    def create_code(self, board):
        # sample colors allowing duplicates.
        self.code = [random.sample(board.colors, 1)[0] for _ in range(0, board.holes)]

    def evaluate_guess(self, guess):
        # helpers initialization
        output, no_hit = [], []
        not_guessed = list(self.code)

        # find all the correct color, correct position pegs
        for i, peg in enumerate(guess):
            if peg == self.code[i]:
                output.append('BLACK')
                not_guessed.remove(peg)
            else:
                no_hit.append(peg)

        # find all the correct color, wrong position pegs
        for peg in no_hit:
            if peg in not_guessed:
                output.append('WHITE')
                not_guessed.remove(peg)

        return output

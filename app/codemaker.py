# coding=utf-8
import random


class Codemaker:
    code = None

    def create_game(self, board):
        # sample colors allowing duplicates.
        self.code = [random.sample(board.colors, 1)[0] for _ in range(0, board.holes)]

    def evaluate_guess(self, guess):
        output = []
        for i, peg in enumerate(guess):
            if peg == self.code[i]:
                output.append('BLACK')
            elif peg in self.code:
                output.append('WHITE')
        return output

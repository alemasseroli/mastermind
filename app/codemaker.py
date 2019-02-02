# coding=utf-8
import random


class Codemaker:
    COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW']
    code = None

    def create_game(self):
        # sample colors allowing duplicates.
        self.code = [random.sample(self.COLORS, 1)[0] for _ in range(0, 4)]

    def evaluate_guess(self, guess):
        output = []
        for i, peg in enumerate(guess):
            if peg == self.code[i]:
                output.append('BLACK')
            elif peg in self.code:
                output.append('WHITE')
        return output

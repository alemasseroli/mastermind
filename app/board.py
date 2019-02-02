class Board:

    def __init__(self, colors, holes):
        self.holes = holes
        self.colors = colors
        self.plays = []

    def add_play(self, guess, output):
        self.plays.append({'guess': guess, 'output': output})

    def historic(self):
        return self.plays

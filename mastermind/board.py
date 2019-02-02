class Board:

    def __init__(self, colors, holes):
        self.plays = []
        self.holes = holes
        self.colors = colors

    def add_play(self, guess, output):
        self.plays.append({'guess': guess, 'output': output})

    def historic(self):
        return self.plays

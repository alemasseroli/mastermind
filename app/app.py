import json

from flask import Flask, request

from board import Board
from codemaker import Codemaker

app = Flask(__name__)

# This parameters can be set at will as long as holes <= len(COLORS) and MAX_ATTEMPTS >= 1.
HOLES = 4
COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PINK']
MAX_ATTEMPTS = 12

codemaker = Codemaker()
board = Board(HOLES, COLORS)

attempts = 0
started = False


@app.route("/create", methods=["POST"])
def create_game():
    global started
    started = True
    codemaker.create_game(board)
    return response("Game Created", 200)


@app.route("/guess", methods=["PUT"])
def guess():
    global started, attempts
    try:
        if not started:
            return response("Game not created.", 400)

        guess = json.loads(request.get_data().upper())

        if is_valid_guess(guess):
            if attempts < MAX_ATTEMPTS:
                attempts += 1
            else:
                attempts = 0
                started = False

            output = codemaker.evaluate_guess(guess)
            board.add_play(guess, output)

            return response(output, 200)
        else:
            return response("Invalid guess", 400)
    except:
        return response("Internal Error", 400)


def is_valid_guess(data):
    return isinstance(data, list) and len(data) == HOLES


def response(data, status_code):
    return json.dumps({"response": data}), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

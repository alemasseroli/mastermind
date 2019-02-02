import json

from flask import Flask, request

from board import Board
from codemaker import Codemaker

app = Flask(__name__)

# This parameters can be set at will as long as holes <= len(COLORS) and MAX_ATTEMPTS >= 1.
HOLES = 4
COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PINK']
MAX_ATTEMPTS = 12

board = None
codemaker = Codemaker()

attempts = 0
started = False


@app.route("/mastermind/create", methods=["POST"])
def create_game():
    global started, attempts, board
    attempts = 0
    started = True
    board = Board(colors=COLORS, holes=HOLES)
    codemaker.create_code(board)
    return response("New game created")


@app.route("/mastermind/historic", methods=["GET"])
def historic():
    if not started:
        return error("Game not created.")
    return response(board.historic())


@app.route("/mastermind/guess", methods=["PUT"])
def guess():
    global started, attempts
    try:
        if not started:
            return error("Game not created.")

        guess = parse_guess(request)
        if is_valid_guess(guess):
            output = codemaker.evaluate_guess(guess)
            board.add_play(guess, output)

            if game_won(output):
                end_game()
                return response("You win!")
            else:
                if attempts < MAX_ATTEMPTS:
                    attempts += 1
                else:
                    end_game()
                    return response("You lose.")

            return response(output)
        else:
            return error("Invalid guess")
    except:
        return error("Internal error", 500)


def parse_guess(request):
    return request.get_data().upper().split(" ")


def game_won(output):
    return output == ['BLACK', 'BLACK', 'BLACK', 'BLACK']


def end_game():
    global started
    started = False


def is_valid_guess(data):
    return isinstance(data, list) and len(data) == HOLES


def response(data):
    return json.dumps({"response": data}), 200


def error(data, status_code=400):
    return json.dumps({"msg": data}), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

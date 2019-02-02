import json

from codemaker import Codemaker
from flask import Flask, request

app = Flask(__name__)
codemaker = Codemaker()


@app.route("/create", methods=["POST"])
def create_game():
    codemaker.create_game()
    return response("Game Created", 200)


@app.route("/guess", methods=["PUT"])
def guess():
    try:
        data = json.loads(request.get_data().upper())
        if is_valid_guess(data):
            output = codemaker.evaluate_guess(data)
            return response(output, 200)
        else:
            return response("Invalid guess", 400)
    except:
        return response("Internal Error", 400)


def is_valid_guess(data):
    # TODO
    return True


def response(data, status_code):
    return json.dumps({"response": data}), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

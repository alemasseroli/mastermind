import os
import json
import traceback

from flask import Flask, request

app = Flask(__name__)

@app.route("/create", , methods=["POST"])
def create_game():
    return response({"msg": "Game Created"}, 200)

@app.route("/guess", methods=["POST"])
def guess():
    try:
        data = json.loads(request.get_data().lower())

        return response(output, 200)

    except:
        return response({"msg": "Error in scoring"}, 400)



def response(data, status_code):
    return json.dumps(data), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

from redirector import redirect
from flask import Flask, request, Response


ITEMS_PATH = 'http://127.0.0.1:5001/'
USERS_PATH = 'http://127.0.0.1:5003/'
app = Flask(__name__)


@app.errorhandler(404)
@app.route("/items/<path>", methods=['GET'])
def items_proxy(path):
    response = redirect(request, ITEMS_PATH)
    return Response(response['content'], response['status_code'], response['headers'])



if __name__ == "__main__":
    app.run(port=5000, debug=True)
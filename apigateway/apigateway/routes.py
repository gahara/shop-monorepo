from redirector import redirect

from flask import Flask, request, Response
from werkzeug.exceptions import NotFound
import json

ITEMS_PATH = 'http://127.0.0.1:5001/'
app = Flask(__name__)


#@app.route("/items/", methods=['GET'])
@app.errorhandler(404)
@app.route("/items/<path>", methods=['GET'])
def items_proxy(path):
    response = redirect(request, ITEMS_PATH)
    return Response(response['content'], response['status_code'], response['headers'])
    #return nice_json({'ok': request.path})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
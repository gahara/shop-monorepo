from common.utils import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open(f"{root_dir()}/temp/items.json", "r") as f:
    items = json.load(f)


@app.route("/", methods=['GET'])
def index():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "items": "/items",
            "item": "/items/<id>"
        }
    })


@app.route("/items/<itemid>", methods=['GET'])
def item_info(itemid):
    if itemid not in items:
        raise NotFound

    result = items[itemid]
    result["uri"] = f"/movies/{itemid}"

    return nice_json(result)


@app.route("/items", methods=['GET'])
def movie_record():
    return nice_json(items)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
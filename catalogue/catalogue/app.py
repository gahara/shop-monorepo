
from werkzeug.exceptions import NotFound
import json

from common.utils import nice_json
from catalogue import app
from models import Item

#https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# как пользоваться flask-sqlalchemy
#как быстро добавить в базу
##https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database - инструкция с миграциями

#from catalogue import db
# with app.app_context():
#     i = Item(title='tomato', price=123, rating=10)
#     i2 = Item(title='potato', price=1230, rating=6)
#     db.session.add(i)
#     db.session.add(i2)
#     db.session.commit()

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
    #https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
    result = Item.query.get_or_404(itemid).to_dict()
    result["uri"] = f"/items/{itemid}"

    return nice_json(result)


@app.route("/items/", methods=['GET'])
def movie_record():
    result_raw = Item.query.all()
    result = [item.to_dict() for item in result_raw]
    return nice_json(result)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
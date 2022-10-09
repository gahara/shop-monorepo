from . import db
#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, index=True)
    title = db.Column(db.String(120), index=True)
    price = db.Column(db.Integer, index=True)
    amount = db.Column(db.Integer, index=False) #надо уменьшать при чекауте

    def __repr__(self):
        return f'{self.title}'

    def to_dict(self):
        return dict(id=self.id, title=self.title, price=self.price, rating=self.rating, amount=self.amount)


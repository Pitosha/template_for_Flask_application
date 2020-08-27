from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    surname = db.Column(db.String(40))
    age = db.Column(db.Integer)

    def __repr__(self):
        return "<User id: {}, User_name: {} User_surname {}>".format(self.id, self.first_name, self.surname)

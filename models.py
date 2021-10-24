from flask_sqlalchemy import SQLAlchemy


defualt = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmDfIMCkTK-J9lc2DyWOULZVtILVdWa-E-qg&usqp=CAU"

db = SQLAlchemy()

# MODELS GO BELOW!

class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default=True)

    def image(self):
        return self.photo_url or defualt

def connect_db(app):
    db.app = app
    db.init_app(app)

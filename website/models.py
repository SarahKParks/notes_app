#import from current package (website folder), import db object
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    # primary key is unique identifier
    id = db.Column(db.Integer, primary_key=True)
    # invalid to create a user with an email that already exists
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # add note id 

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # gets current date and time
    # associate note with a unqiue user w/ a foreign key
    # db.ForeignKey enforces that a valid user id must be given to this id
    # user represents User, id is the field of the user object
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

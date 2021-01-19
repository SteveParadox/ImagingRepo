from datetime import datetime

from flask_login import UserMixin

from marshmallow_sqlalchemy import ModelSchema

from dev import db, login_manager


@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    password = db.Column(db.String(), nullable=False)
    loggedIn = db.Column(db.Boolean, default=False)
    upload = db.relationship('Upload', backref='data', lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"




class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publicId = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    image = db.Column(db.String)
    imageData = db.Column(db.LargeBinary)
    dateUploaded = db.Column(db.DateTime, nullable=False, default=datetime.now)
    UserId = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Upload('{self.name}', '{self.publicId}')"
  

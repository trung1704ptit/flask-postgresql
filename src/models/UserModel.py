# src/models/UserModel

from marshmallow import fields, Schema
from ..app import bcrypt
import datetime
from .BlogpostModel import BlogpostSchema
from . import db


class UserModel(db.Model):
    """
    User Model
    """
    # Table name
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Coumn(db.Datetime)
    modified_at = db.Column(db.Datetime)
    blogposts = db.relationship('BlogpostModel', backref = 'users', lazy=True)

    # class Constructor
    def __init__(self, data):
        """
        Class Constructor
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = self.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.__generate_hash(data.get('password'))
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, round=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

class UserSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    created_at = fields.Datetime(dump_only=True)
    modified_at = fields.Datetime(dump_only=True)
    blogposts = fields.Nested(BlogpostSchema, many=True)
# imports 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(), nullable = True, default = '')
    token = db.Column(db.String(), default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'

class Book(db.Model):
    id = db.Column(db.String(), primary_key = True)
    year_published = db.Column(db.String(4), nullable = True)
    title = db.Column(db.String(150), nullable = True)
    genre = db.Column(db.String(150), nullable = True)
    author = db.Column(db.String(150), nullable = True)
    ISBN = db.Column(db.String(100), nullable = True)
    page_count = db.Column(db.String(20), nullable = True)
    availability = db.Column(db.String(20), nullable = True)
    book_token = db.Column(db.String(), db.ForeignKey('user.token'), nullable = False)

    def __init__(self,year_published,title,genre,author,ISBN,page_count,availability,book_token, id = ''):
        self.id = self.set_id()
        self.year_published = year_published
        self.title = title
        self.genre = genre
        self.author = author
        self.ISBN = ISBN
        self.page_count = page_count
        self.availability = availability
        self.book_token = book_token


    def __repr__(self):
        return f'The following book has been added to the list: {self.author} {self.title} {self.genre}'

    def set_id(self):
        return (secrets.token_urlsafe())

class BookSchema(ma.Schema):
    class Meta:
        fields = ['id', 'year_published','title','genre', 'author', 'ISBN', 'page_count', 'availability']

Book_schema = BookSchema()
Books_schema = BookSchema(many=True)
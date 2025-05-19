# models.py

# Importing SQLAlchemy for working with the database
from flask_sqlalchemy import SQLAlchemy

# Initializing the SQLAlchemy object
db = SQLAlchemy()

# ----------------------
# User Model
# ----------------------
# This model represents a user in the system
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username must be unique and not empty
    password = db.Column(db.String(80), nullable=False)  # Plaintext password (not secure for real apps)

# ----------------------
# Book Model
# ----------------------
# This model represents a book saved by a user
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each book
    title = db.Column(db.String(200))  # Title of the book
    author = db.Column(db.String(100))  # Author(s) of the book
    page_count = db.Column(db.Integer)  # Total number of pages
    average_rating = db.Column(db.Float)  # Average rating from Google Books API
    thumbnail = db.Column(db.String(300))  # URL to the book cover thumbnail image
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Link the book to a specific user

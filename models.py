from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):
class game(db.model):
    id = db.Column(db.integer,primary_key = True)
    title = db.Column(db.string(100), nullable = False)
    dev = db.Column(db.string(100), nullable = False)
    year = db.Column(db.integer, nullable = True)
    genre = db.Column(db.string(100), nullable = True)
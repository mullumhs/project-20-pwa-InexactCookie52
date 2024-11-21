from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):
class game(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    dev = db.Column(db.String(100), nullable = False)
    year = db.Column(db.Integer, nullable = True)
    genre = db.Column(db.String(100), nullable = True)
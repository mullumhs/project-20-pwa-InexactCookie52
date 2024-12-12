from flask import render_template, request, redirect, url_for, flash
from models import db, Game# Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        # This route should retrieve all items from the database and display them on the page.
        games = Game.query.all()
        return render_template('index.html', games = games)



    @app.route('/add', methods=['POST'])
    def add_game():
        if request.method == 'POST':
            new_game = Game(
                title=request.form['title'],
                description=request.form['description'],
                year=request.form['year'],
                publisher=request.form['publisher'],
                genre=request.form['genre'],
                image=request.form['image']
        )
            db.session.add(new_game)
            db.session.commit()
            return redirect(url_for("get_items"))
        #return render_template('index.html', message='Item added successfully')
    

    @app.route('/update', methods=['POST'])
    def update_item():
        id = request.form["id"]
        game = Game.query.get(id)
        game.title=request.form['title']
        game.description=request.form['description']
        game.year=request.form['year']
        game.publisher=request.form['publisher']
        game.genre=request.form['genre']
        game.image=request.form['image']
        db.session.commit()
        return redirect(url_for("get_items"))

    @app.route('/edit', methods=['GET'])
    def edit():

        # This route should retrieve all items from the database and display them on the page.
        id = request.args.get('id')
        game = Game.query.get(id)
        return render_template('edit.html', game = game)

    @app.route('/delete', methods=['GET'])
    def delete_item():
        id = request.args.get('id')
        game = Game.query.get(id)
        db.session.delete(game)
        db.session.commit()
        # This route should handle deleting an existing item identified by the given ID.
        return redirect(url_for("get_items"))
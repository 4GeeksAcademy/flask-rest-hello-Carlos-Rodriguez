from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, People, Planets, Favorites

app = Flask(__name__)
app.url_map.strict_slashes = False

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    return jsonify([user.serialize() for user in all_users])

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    # Assuming you have some authentication mechanism to get the current user
    user_id = 1  # Example user ID
    user_favorites = Favorites.query.filter_by(user_id=user_id).all()
    return jsonify([favorite.serialize() for favorite in user_favorites])

@app.route('/favorites/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    # Assuming you have some authentication mechanism to get the current user
    user_id = 1  # Example user ID
    new_favorite = Favorites(user_id=user_id, planets_id=planet_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify(new_favorite.serialize()), 200

# Similarly, you can implement other endpoints for /favorites/people, /favorite/planet/<int:planet_id>/delete, etc.

if __name__ == '__main__':
    app.run(debug=True)

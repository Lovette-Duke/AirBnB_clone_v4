#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, Blueprint
from models import storage
import uuid

# Create a Blueprint instance
bp = Blueprint('hbnb', __name__)


# Define a class-based view
class HBNBView:
    def __init__(self):
        self.state_objs = storage.all('State').values()
        self.states = dict([(state.name, state) for state in self.state_objs])
        self.amens = storage.all('Amenity').values()
        self.places = storage.all('Place').values()
        self.users = dict([(user.id, f"{user.first_name} {user.last_name}") for user in storage.all('User').values()])

    def render_template(self):
        return render_template('4-hbnb.html',
                               cache_id=uuid.uuid4(),
                               states=self.states,
                               amens=self.amens,
                               places=self.places,
                               users=self.users)


# Register a route with the Blueprint
@bp.route('/4-hbnb')
def hbnb_filters():
    view = HBNBView()
    return view.render_template()


# Create a Flask app instance
def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    # Run the Flask app
    app = create_app()
    app.run(host='0.0.0.0', port=5000)


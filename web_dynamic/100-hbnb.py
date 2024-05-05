#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, Blueprint
from models import storage
import uuid

# Create a Blueprint instance
hbnb_bp = Blueprint('hbnb', __name__)

# Define the route within the Blueprint
@hbnb_bp.route('/100-hbnb')
def hbnb_filters(the_id=None):
    """
    Handles request to custom template with states, cities & amenities
    """
    state_objs = storage.all('State').values()
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = {user.id: f"{user.first_name} {user.last_name}" for user in storage.all('User').values()}
    
    return render_template('100-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=state_objs,
                           amens=amens,
                           places=places,
                           users=users)

# Create the Flask app and register the Blueprint
app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(hbnb_bp)

# Define host and port
host = '0.0.0.0'
port = 5000

if __name__ == "__main__":
    """
    Main Flask App
    """
    app.run(host=host, port=port)


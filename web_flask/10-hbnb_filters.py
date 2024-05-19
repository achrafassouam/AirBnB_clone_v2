#!/usr/bin/python3
"""
Flask Application
"""
from models import storage
from flask import Flask, render_template
from os import environ

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(exception):
    """
    Remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays the main HBNB filters HTML page
    """
    states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
    amenities = sorted(list(storage.all('Amenity').values()), key=lambda x: x.name)
    cities = sorted(list(storage.all('City').values()), key=lambda x: x.name)

    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities,
                           cities=cities)


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, debug=True)

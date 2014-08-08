import json

from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configurations
#app.config.from_object('config')

from spotify_poetry.app.models import Poem
from spotify_poetry.app.controller import SpotifyPoet

poet = SpotifyPoet()

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('index.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/search', methods=['POST'])
def find_tracks():
    poetry_string = request.form['poetry']
    result = None
    try :
        poetry = Poem(poetry_string)
        poetry_tracks = poet.sing_poem(poetry);
        result = json.dumps({'result':poetry_tracks})
    except Exception as e:
        print "Error occurred with poem: " + poetry_string + " - " + e
    return result

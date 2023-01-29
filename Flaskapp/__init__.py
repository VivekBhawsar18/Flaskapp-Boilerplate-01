from flask import Flask
from config import Config
from Flaskapp.extensions import db

app = Flask(__name__)

# App configuration
app.config.from_object(Config)

# Initialize Flask extensions here
db.init_app(app)


@app.route('/')
def home():
        return '<h1>Home page of Flask Application Factory Pattern</h1>'

@app.route('/test/')
def test_page():
        return '<h1>Test page of Flask Application Factory Pattern</h1>'
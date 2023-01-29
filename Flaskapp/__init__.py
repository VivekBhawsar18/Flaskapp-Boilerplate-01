from flask import Flask
from config import Config
from Flaskapp.extensions import db

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    @app.route('/')
    def home():
        # return str(os.environ.get('SECRET_KEY'))
        # return str(os.environ.get('SQLALCHEMY_DATABASE_URI'))
        return '<h1>Home page of Flask Application Factory Pattern</h1>'

    @app.route('/test/')
    def test_page():
        # return str(os.environ.get('SECRET_KEY'))
        # return str(os.environ.get('SQLALCHEMY_DATABASE_URI'))
        return '<h1>Testing the Flask Application Factory Pattern</h1>'


    return app
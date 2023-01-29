from flask import Flask
from config import Config
from Flaskapp.extensions import db

app = Flask(__name__)

# App configuration
app.config.from_object(Config)

# Initialize Flask extensions here
db.init_app(app)

# Register blueprints here
from Flaskapp.Test.routes import bp as Test_bp
app.register_blueprint(Test_bp , url_prefix='/test')


@app.route('/')
def home():
        return '<h1>Home page of Flask Application Factory Pattern</h1>'
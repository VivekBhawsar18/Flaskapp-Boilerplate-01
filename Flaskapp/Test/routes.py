from flask import render_template , Blueprint
from config import Config

bp = Blueprint('Test' , __name__)

@bp.route('/')
def index_test():
    return render_template('index.html')

@bp.route('/db')
def test_db():
    return( f"{Config.SQLALCHEMY_DATABASE_URI}{Config.SQLALCHEMY_TRACK_MODIFICATIONS}\t{Config.SECRET_KEY}")


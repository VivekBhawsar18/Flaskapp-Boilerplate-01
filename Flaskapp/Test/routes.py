from flask import render_template , Blueprint

bp = Blueprint('Test' , __name__)

@bp.route('/')
def index_test():
    return render_template('index.html')
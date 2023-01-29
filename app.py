from Flaskapp import app


if __name__ == '__main__':
    app.run()

# -------------------------------------------------------------------------

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#         # return str(os.environ.get('SECRET_KEY'))
#         # return str(os.environ.get('SQLALCHEMY_DATABASE_URI'))
#         return '<h1>Home page of Flask Application Factory Pattern</h1>'

# @app.route('/test/')
# def test_page():
#         # return str(os.environ.get('SECRET_KEY'))
#         # return str(os.environ.get('SQLALCHEMY_DATABASE_URI'))
#         return '<h1>Testing the Flask Application Factory Pattern</h1>'

# if __name__ == '__main__':
#     app.run()

# from Flaskapp import app

# if __name__ == '__main__':
#     app.run() 
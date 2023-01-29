# import os

# basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/cndb'
    SECRET_KEY= 'B@Vv$st^<b^NJt/'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vivek01:Vikas#9789@mysql-server-demoflask.mysql.database.azure.com/cndb'
    # print(SQLALCHEMY_DATABASE_URI)
    # print(SECRET_KEY)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
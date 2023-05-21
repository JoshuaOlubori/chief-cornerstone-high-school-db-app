from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
mysql_conn = MySQL()
login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'

    # MySQL configuration
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'pluto'
    app.config['MYSQL_DB'] = 'iterc'

    # SQLite configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    bootstrap.init_app(app)
    mysql_conn.init_app(app)
    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth)

    from .views import bp
    app.register_blueprint(bp)


    return app
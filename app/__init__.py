from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'secret'
    app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://LAPTOP-4GKIPSIP\SQLEXPRESS/PerCapita?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    from app import routes
    routes.init_app(app)

    return app
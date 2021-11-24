from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return Agiota.query.get(user_id)

class Agiota(db.Model, UserMixin):
    __tablename__ = "agiota_login"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(84), nullable = False, unique=True, index=True)
    password = db.Column(db.String(255), nullable = False)

    def __str__(self):
        return self.email

class Ibge(db.Model, UserMixin):
    __tablename__ = "agiota_do_ibge"
    id = db.Column(db.Integer, primary_key = True)
    UF = db.Column(db.String(84), nullable = False)
    media = db.Column(db.Float, nullable = False)
    capital = db.Column(db.String(84), nullable = False)
    renda_per_capita = db.Column(db.Float, nullable = False)

    def __str__(self):
        return self.UF

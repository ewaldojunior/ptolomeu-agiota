from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from app.models import Agiota, Ibge
from app import db

def init_app(app):
    @app.route("/", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            user = Agiota.query.filter_by(email=email).first()

            if not user:
                flash(message="Credências incorretas... Tente novamente.", category='danger')
                return redirect(url_for('login'))

            if not check_password_hash(user.password, password):
                flash(message="Credências incorretas... Tente novamente.", category='danger')
                return redirect(url_for('login'))
            
            login_user(user)
            return redirect(url_for('index'))
        
        return render_template("login.html")


    @app.route("/home")
    def index():
        estado = Ibge.UF
        media_pib = Ibge.media
        media_renda_percapita = Ibge.renda_per_capita
        capital = Ibge.capital

        top5ricos = db.session.query(estado, capital, media_pib, media_renda_percapita).order_by(Ibge.renda_per_capita.desc()).limit(5).all()

        top5pobres = db.session.query(estado, capital, media_pib, media_renda_percapita).order_by(Ibge.renda_per_capita.asc()).limit(5).all()

        flash(message="Ptolomeu logado com sucesso!", category='success')

        return render_template("agiota.html", top5ricos=top5ricos, top5pobres=top5pobres)

    @app.route('/amigo')
    def amigo():
        return render_template('amigo.html')


    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("login"))
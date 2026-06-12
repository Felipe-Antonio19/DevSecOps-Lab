from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
from flask import session

import sqlite3
app = Flask(__name__)

app.secret_key = "uiow4ehjt98uw34t8943wtjw4g"

def get_connection():
    con = sqlite3.connect("devsecopsDb.db")
    cursor = con.cursor()
    return cursor, con

@app.route("/", methods=["GET", "POST"])
def register():
    cursor, con = get_connection();
    if request.method == "POST":
        name = request.values.get("name", "").strip()
        email = request.values.get("email", "").strip()
        password = request.values.get("password", "").strip()

        if not name or not email or not password:
            flash("Preencha todos os campos para continuar.")
            return redirect(url_for("register"))

        # QUERY COM SQL INJECTION
        query = f"INSERT INTO users (name, email, senha) VALUES ('{name}', '{email}', '{password}')"
        print(query) # PARA VER O QUE ESTÁ SENDO EXECUTADO NO BANCO DE DADOS
        cursor.execute(query)
        con.commit()
        con.close()
        flash(f"Usuário {name} cadastrado com sucesso.")
        return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    cursor, con = get_connection();
    if request.method == "POST":
        email = request.values.get("email", "").strip()
        password = request.values.get("password", "").strip()
        
        if not email or not password:
            flash("Preencha todos os campos para continuar.")
            return redirect(url_for("login"))
        
        query = f"SELECT * FROM users WHERE email = '{email}' AND senha = '{password}'"
        print(query)
        res = cursor.execute(query).fetchone()
        
        if res is None:
            flash("Login ou senha inválidos.")
            return redirect(url_for("login"))
        else:
            session["logged_in"] = True
            return redirect(url_for("dashboard"))

    return render_template("login.html")
        
@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        flash("Faça login para continuar.")
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        name=session.get("name")
    )

    return render_template("login.html")



# ROTA DE TESTE PARA VER SE CONSEGUIMOS PEGAR OS USUÁRIOS CADASTRADOS COM SQL INJECTION
@app.route("/users", methods=["GET"])
def get_users():
    con = sqlite3.connect("devsecopsLab.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    usuarios = cursor.fetchall()
    con.close()
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)

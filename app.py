from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
import sqlite3
app = Flask(__name__)

app.secret_key = "uiow4ehjt98uw34t8943wtjw4g"

def get_connection():
    con = sqlite3.connect("devsecopsLab.db")
    cursor = con.cursor()
    return cursor, con

@app.route("/", methods=["GET", "POST"])
def register():
    cursor, con = get_connection();
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not name or not email or not password:
            flash("Preencha todos os campos para continuar.")
            return redirect(url_for("register"))

        # QUERY COM SQL INJECTION
        cursor.execute(f"INSERT INTO users (name, email, senha) VALUES ('{name}', '{email}', '{password}')")
        con.commit()
        con.close()
        flash(f"Usuário {name} cadastrado com sucesso.")
        return redirect(url_for("register"))

    return render_template("register.html")

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

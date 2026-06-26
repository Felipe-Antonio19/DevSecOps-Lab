from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
from flask import session
from dataclasses import dataclass

import sqlite3
app = Flask(__name__)

@dataclass
class Usuario:
    id: int
    nome: str
    email: str
    senha: str

app.secret_key = "uiow4ehjt98uw34t8943wtjw4g"

def get_connection():
    con = sqlite3.connect("devsecopsDb.db")
    # con.row_factory = sqlite3.Row
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

        cursor.execute(f"INSERT INTO users (name, email, senha) VALUES '{name}', '{email}', '{password}'")
        con.commit()
        con.close()
        flash(f"Usuário {name} cadastrado com sucesso.")

        return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    cursor, con = get_connection()

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not email or not password:
            flash("Preencha todos os campos para continuar.")
            return redirect(url_for("login"))

        # Busca usuario via email apenas.
        user = cursor.execute(f"SELECT id, name, email, senha FROM users WHERE email = '{email}'").fetchone()
        
        # 2. Diferencia comportamento se usuário existe ou não
        if not user:
            con.close()
            flash("Usuário não encontrado")
            return redirect(url_for("login"))
        
        user = Usuario(*user)
        # Aqui sabe-se que o usuario existe apenas por verificação via email
        db_password = user.senha

        # 4. Verificação separada da senha (também contribui para enumeração)
        if password != db_password:
            con.close()
            flash("Senha incorreta")
            return redirect(url_for("login"))

        # 5. Login bem-sucedido
        con.close()

        session["logged_in"] = True
        session["user_id"] = user[0]
        session["name"] = user[1]
        session["email"] = user[2]

        return redirect(url_for("dashboard"))

    return render_template("login.html")
        
@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        flash("Faça login para continuar.")
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        name=session.get("name"),
        email=session.get("email")
    )

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    owner_id = session.get("user_id")
    cursor, con = get_connection();

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()

        cursor.execute(f"INSERT INTO tasks (title, description, owner_id) VALUES '{title}','{description}','{owner_id}'")
        con.commit()
        con.close()
        flash("Task inserida com sucesso.")
        return redirect(request.url)

    cursor.execute("SELECT * FROM tasks") # <-- Query sem verificação de owner_id (Horizontal Privilege Escalation)
    tasks = cursor.fetchall()
    con.close()
    return render_template(
        "tasks.html",
        name=session.get("name"),
        email=session.get("email"),
        tasks=tasks
    )

@app.route("/tasks/delete", methods=["POST"])
def delete_tasks():
    cursor, con = get_connection()
    
    if not session.get("logged_in"):
        flash("Faça login para continuar.")
        return redirect(url_for("login"))

    task_ids = request.form.getlist("task_ids")
    if not task_ids:
        flash("Selecione ao menos uma task para excluir.")
        return redirect(url_for("tasks"))

    ids = [int(task_id) for task_id in task_ids if task_id.isdigit()]
    if not ids:
        flash("Nenhuma task válida selecionada.")
        return redirect(url_for("tasks"))

    placeholders = ",".join("?" for _ in ids)
    cursor.execute(
    f"DELETE FROM tasks WHERE id IN ({placeholders})", ids) # <-- Sem verificação de owner_id (IDOR)
    deleted = cursor.rowcount
    con.commit()
    con.close()

    flash(f"{deleted} task(s) excluída(s).")
    return redirect(url_for("tasks"))

@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu com sucesso.")
    return redirect(url_for("login"))

# @app.route("/get_users", methods=["GET"])
# def get_users():
#     con = sqlite3.connect("devsecopsDb.db")
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM users")
#     usuarios = cursor.fetchall()
#     con.close()
#     return jsonify(usuarios)

# @app.route("/get_tasks", methods=["GET"])
# def get_tasks():
#     con = sqlite3.connect("devsecopsDb.db")
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM tasks")
#     usuarios = cursor.fetchall()
#     con.close()
#     return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)

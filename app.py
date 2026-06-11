from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "uiow4ehjt98uw34t8943wtjw4g"

users = []

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not name or not email or not password:
            flash("Preencha todos os campos para continuar.")
            print("Teste")
            return redirect(url_for("register"))

        users.append({"name": name, "email": email})
        flash(f"Usuário {name} cadastrado com sucesso.")
        return redirect(url_for("register"))

    return render_template("register.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "segredo_salao"

DB = "agendamentos.db"


def conectar():
    return sqlite3.connect(DB)


# ---------- HOME ----------
@app.route("/")
def home():
    return render_template("index.html")


# ---------- LOGIN (SÓ SUA MÃE) ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "Je" and senha == "1720":
            session["logado"] = True
            return redirect("/lista")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------- AGENDAR (CLIENTE) ----------
@app.route("/agendar", methods=["GET", "POST"])
def agendar():
    conn = conectar()
    cur = conn.cursor()

    if request.method == "POST":
        data = request.form["data"]
        horario = request.form["horario"]

        # BLOQUEAR HORÁRIO
        cur.execute(
            "SELECT * FROM agendamentos WHERE data=? AND horario=?",
            (data, horario)
        )
        if cur.fetchone():
            conn.close()
            return "Horário já ocupado. <a href='/agendar'>Voltar</a>"

        # MULTI SERVIÇOS
        servicos = request.form.getlist("servicos")
        servico = ", ".join(servicos)

        cur.execute("""
            INSERT INTO agendamentos (nome, telefone, servico, data, horario)
            VALUES (?, ?, ?, ?, ?)
        """, (
            request.form["nome"],
            request.form["telefone"],
            servico,
            data,
            horario
        ))

        conn.commit()
        conn.close()
        return redirect("/")

    conn.close()
    return render_template("agendar.html")


# ---------- LISTA (ADMIN) ----------
@app.route("/lista")
def lista():
    if not session.get("logado"):
        return redirect("/login")

    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM agendamentos ORDER BY data, horario")
    dados = cur.fetchall()
    conn.close()

    return render_template("lista.html", agendamentos=dados)


# ---------- EDITAR ----------
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if not session.get("logado"):
        return redirect("/login")

    conn = conectar()
    cur = conn.cursor()

    if request.method == "POST":
        servicos = request.form.getlist("servicos")
        servico = ", ".join(servicos)

        cur.execute("""
            UPDATE agendamentos
            SET nome=?, telefone=?, servico=?, data=?, horario=?
            WHERE id=?
        """, (
            request.form["nome"],
            request.form["telefone"],
            servico,
            request.form["data"],
            request.form["horario"],
            id
        ))

        conn.commit()
        conn.close()
        return redirect("/lista")

    cur.execute("SELECT * FROM agendamentos WHERE id=?", (id,))
    agendamento = cur.fetchone()
    conn.close()

    return render_template("editar.html", a=agendamento)

# ---------- EXCLUIR ----------
@app.route("/excluir/<int:id>")
def excluir(id):
    if not session.get("logado"):
        return redirect("/login")

    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM agendamentos WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/lista")


if __name__ == "__main__":
    app.run(port=9000, debug=True)

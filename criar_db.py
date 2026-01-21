import sqlite3

conn = sqlite3.connect("agendamentos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    servico TEXT NOT NULL,
    data TEXT NOT NULL,
    horario TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso.")

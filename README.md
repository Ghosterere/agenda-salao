# 💅 Agenda de Salão

Sistema web simples para **controle de agendamentos** de um salão de beleza  
(manicure, pedicure e cabeleireira), desenvolvido para **uso interno**, de forma prática, organizada e fácil de usar.

---

## ✨ Funcionalidades

- ✅ Criar agendamentos  
- ✏️ Editar agendamentos  
- ❌ Excluir agendamentos  
- 📅 Visualizar agendamentos por dia  
- 🚫 Bloquear horários duplicados ou conflitantes  
- 💾 Salvar todos os dados no banco de dados (SQLite)  
- 🎨 Interface simples, clean e intuitiva  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Jinja2** (templates HTML)
- **CSS puro**
- **Uvicorn**

---

## 📁 Estrutura do Projeto

```text
agenda-salao/
│
├── app/
│   ├── main.py          # Arquivo principal da aplicação
│   ├── database.py      # Conexão com o banco de dados
│   ├── models.py        # Modelos do banco (SQLAlchemy)
│   ├── crud.py          # Regras de criação, edição e exclusão
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── novo.html
│   │   └── editar.html
│   │
│   └── static/
│       └── style.css
│
├── agenda.db            # Banco de dados SQLite (criado automaticamente)
├── requirements.txt
└── README.md

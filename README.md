<<<<<<< HEAD
# Agenda Salão 💅✂️
Sistema de agendamento de horários para manicure, pedicure e cabelereira,
feito em Python usando Flask.

## Funcionalidades

- Agendamento de horários pelo cliente
- Login administrativo (somente a profissional)
- Bloqueio de horários já ocupados
- Editar agendamentos
- Excluir horários
- Lista organizada de clientes
- Layout simples e profissional

## Tecnologias utilizadas

- Python 🐍
- Flask
- HTML
- CSS
- SQLite

## Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/Ghosterere/agenda-salao.git
=======

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
```

## 🧠 Regras de Agendamento

Não é permitido criar dois agendamentos no mesmo dia e horário

Caso o horário esteja ocupado, o sistema bloqueia o cadastro

Todos os dados ficam salvos no banco de dados local (SQLite)

---

## 🎯 Objetivo do Projeto

Este projeto foi criado para facilitar o dia a dia de um salão de beleza,
substituindo agendas de papel por uma solução digital simples, funcional e fácil de manter.

---

## 👤 Autor
Projeto desenvolvido por Caio Santos
Para uso pessoal / familiar ❤️

# 🐍 PyLearn WebApp – Plataforma de Estudio y Práctica de Python

Bienvenido a **PyLearn**, una aplicación web pensada para que los usuarios puedan aprender y practicar Python, incluyendo módulos teóricos, ejercicios interactivos y una sección especializada en estadística aplicada con Python.

---

## ✨ Funcionalidades principales

- ✅ Registro y login de usuarios
- 📘 Módulo de estudio con contenidos teóricos
- 🧪 Módulo de ejercicios de Python por niveles
- 💻 Módulo de práctica libre con ejecución de código
- 📊 Módulo adicional de estadística aplicada en Python
- 💾 ORM con SQLAlchemy y base de datos inicial en SQLite (fácilmente migrable a PostgreSQL u otros)
- 🌐 Interfaz web moderna, accesible y responsiva

---

## 🛠️ Tecnologías utilizadas (propuesta inicial)

| Componente    | Tecnología propuesta                |
|---------------|-------------------------------------|
| Backend       | Python + FastAPI                    |
| Frontend      | React / HTMX / Jinja2 (según stack) |
| ORM           | SQLAlchemy                          |
| Base de datos | SQLite (dev), PostgreSQL (prod)     |
| Autenticación | JWT                                 |

> Puedes cambiar el stack según preferencias. El diseño actual es modular para facilitar futuras migraciones.

---

## 🚀 Instalación y uso local

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/pylearn-webapp.git
cd pylearn-webapp
```

### 2. Iniciar el backend (modo desarrollo)

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

La API estará disponible en [http://localhost:8000](http://localhost:8000).

---

## 📄 Licencia

MIT

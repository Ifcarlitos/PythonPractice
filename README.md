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
| Backend       | Python + FastAPI / Flask            |
| Frontend      | React / HTMX / Jinja2 (según stack) |
| ORM           | SQLAlchemy                          |
| Base de datos | SQLite (dev), PostgreSQL (prod)     |
| Autenticación | JWT / Flask-Login                   |

> Puedes cambiar el stack según preferencias. El diseño actual es modular para facilitar futuras migraciones.

---

## 🚀 Instalación y uso local

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/pylearn-webapp.git
cd pylearn-webapp

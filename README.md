# Django Tutorial

A beginner-friendly Django web application tutorial project that demonstrates the fundamentals of Django development.

## 🚀 Overview

This project serves as a learning resource for Django web development. It's a clean, minimal Django project setup that you can use as a starting point to learn Django concepts, build features, and understand web development with Python.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12+** - [Download Python](https://www.python.org/downloads/)
- **uv** (Python package manager) - [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd django-tutorial
```

### 2. Install Dependencies

This project uses `uv` for dependency management. Install the required packages:

```bash
uv sync
```

### 3. Run Database Migrations

```bash
uv run python manage.py migrate
```

### 4. Create a Superuser (Optional)

```bash
uv run python manage.py createsuperuser
```

### 5. Start the Development Server

```bash
uv run python manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📁 Project Structure

```
django-tutorial/
├── djangotutorial/          # Main Django project directory
│   ├── __init__.py
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
├── pyproject.toml          # Project dependencies and metadata
├── uv.lock                 # Locked dependency versions
├── db.sqlite3              # SQLite database (created after migration)
└── README.md               # This file
```

## 🔧 Configuration

### Environment Setup

The project uses SQLite as the default database for simplicity. For production, consider using PostgreSQL or MySQL.

### Key Settings

- **DEBUG**: Set to `True` for development
- **SECRET_KEY**: Configured for development (change for production)
- **ALLOWED_HOSTS**: Empty list for development

## 🎯 What's Included

- **Django 5.2.5+** - Latest stable Django version
- **SQLite Database** - Lightweight database for development
- **Admin Interface** - Accessible at `/admin/`
- **Modern Python Setup** - Using `uv` for dependency management

## 🚀 Next Steps

This is a clean Django project ready for you to build upon. Here are some ideas to get started:

1. **Create Your First App**:
   ```bash
   uv run python manage.py startapp myapp
   ```

2. **Add Models** - Define your data structures
3. **Create Views** - Handle HTTP requests
4. **Design Templates** - Build your user interface
5. **Configure URLs** - Set up routing

## 📚 Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)

## 🤝 Contributing

This is a tutorial project, but if you find any issues or have suggestions for improvements, feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Django documentation](https://docs.djangoproject.com/)
2. Search for similar issues in the Django community
3. Create an issue in this repository

---

**Happy coding! 🐍✨**
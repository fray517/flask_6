"""
Инициализация приложения Flask с использованием Application Factory.
"""
from flask import Flask


def create_app() -> Flask:
    """
    Создает и настраивает экземпляр приложения Flask.

    Returns:
        Flask: Настроенное приложение Flask.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Регистрация blueprint для формы
    from flaskr import form
    app.register_blueprint(form.bp)

    return app


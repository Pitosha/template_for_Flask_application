import os

class Config(object):

    #Режим отладки
    DEBUG = True

    # Включение защиты против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True

    # Случайный ключ, которые будет исползоваться для подписи
    # данных, например cookies.
    SECRET_KEY = 'PitFavorit111'

    # URI используемая для подключения к базе данных
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tony:123@localhost:5432/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Основные настройки приложения
    APP_NAME = "Мой Сает"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

#Создаем приложение Flask
app = Flask(__name__)

#Указываем приложению что конфиги будут браться из обьекта, то есть иза класса Config
app.config.from_object(config.Config)

#Подключаем наше приложение к SQLAlchemy
db = SQLAlchemy(app)

migrate = Migrate(app, db)

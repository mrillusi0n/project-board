from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
security = Security()
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_login import LoginManager
from flask_admin import Admin
from .admin_views import AdminHomeView

db = SQLAlchemy()
login_manager = LoginManager()
security = Security()
admin = Admin(name='Project Board', template_mode='bootstrap4', url='/', index_view=AdminHomeView('Home'))
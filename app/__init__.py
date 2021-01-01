from flask import Flask
from flask_security import SQLAlchemyUserDatastore
from flask_admin import helpers as admin_helpers

from .extensions import db, login_manager, security, admin
from .utils import get_random_color

def create_app():
	app = Flask(__name__)

	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = '20ba17ea83bab6812155969188f90a37'

	app.jinja_env.globals.update(get_random_color=get_random_color)

	login_manager.init_app(app)
	login_manager.login_view = 'login'

	db.init_app(app)

	from .models import User, Role, Student, Mentor
	from .admin_views import RestrictedAdminView

	user_datastore = SQLAlchemyUserDatastore(db, User, Role)
	security.init_app(app, user_datastore)

	admin.init_app(app)

	admin.add_view(RestrictedAdminView(User, db.session))
	admin.add_view(RestrictedAdminView(Role, db.session))
	admin.add_view(RestrictedAdminView(Student, db.session))
	admin.add_view(RestrictedAdminView(Mentor, db.session))

	return app

app = create_app()

from . import routes
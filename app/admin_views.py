from flask import redirect, url_for, request
from flask_admin.contrib import sqla
from flask_admin import AdminIndexView
from flask_login import current_user


class AdminHomeView(AdminIndexView):
	def is_accessible(self):
		return (
			current_user.is_authenticated and
			current_user.has_role('admin')
		)

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login', next=request.url))


class RestrictedAdminView(sqla.ModelView):
	def is_accessible(self):
		return (
			current_user.is_authenticated and
			current_user.has_role('admin')
		)

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login', next=request.url))
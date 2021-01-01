from .extensions import db

from sqlalchemy import String, Boolean, Integer, Column, DateTime
from flask_security import RoleMixin, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

class User(db.Model, UserMixin):
	__tablename__ = 'users'
	id = Column(Integer(), primary_key=True)
	username = Column(String(32), nullable=False, unique=True)
	password_hash = Column(String(94), default=lambda: generate_password_hash('panda'))
	email = Column(String(128), nullable=False, unique=True)
	user_type = Column(String(8))
	is_active = Column(Boolean(), default=lambda: True)
	confirmed_at = Column(DateTime(), default=datetime.utcnow)
	roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f'User: {self.username}'


class Role(db.Model, RoleMixin):
	__tablename__ = 'roles'
	id = Column(Integer(), primary_key=True)
	name = Column(String(16), unique=True)


class UserRole(db.Model):
	__tablename__ = 'user_roles'
	id = Column(Integer(), primary_key=True)
	user_id = Column(Integer(), db.ForeignKey('users.id'))
	role_id = Column(Integer(), db.ForeignKey('roles.id'))



class Student(db.Model):
	__tablename__ = 'students'
	id = Column(Integer(), primary_key=True)
	username = Column(String(32), nullable=False, unique=True)
	usn = Column(String(10), nullable=False, unique=True)
	name = Column(String(60), nullable=False)
	team_id = Column(Integer(), db.ForeignKey('teams.id'))

	def __repr__(self):
		return f'Student: {self.usn}'


class Mentor(db.Model):
	__tablename__ = 'mentors'
	id = Column(Integer(), primary_key=True)
	username = Column(String(32), nullable=False, unique=True)
	mentor_id = Column(String(10), nullable=False, unique=True)
	name = Column(String(60), nullable=False)
	teams = db.relationship('Team', backref='mentor', lazy=True)

	def __repr__(self):
		return f'Mentor: {self.mentor_id}'


class Team(db.Model):
	__tablename__ = 'teams'
	id = Column(Integer(), primary_key=True)
	name = Column(String(3), nullable=False, unique=True)
	project = Column(String(60))
	mentor_id = Column(Integer(), db.ForeignKey('mentors.id'))
	members = db.relationship('Student', backref='team', lazy=True)

	def __repr__(self):
		return f'Team: {self.team_id}'
	
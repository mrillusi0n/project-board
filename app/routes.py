from . import app
from app.models import User, Team, Mentor, Student

from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_security import current_user, login_user, logout_user, login_required, roles_required


@app.route('/')
def login():
	if current_user.is_authenticated:
		return redirect(url_for(f'{current_user.user_type}_dash'))
	return render_template('security/login_user.html')


@app.route('/validate_login', methods=['POST'])
def validate_login():
	username = request.form['username']
	password = request.form['pass']

	if not (user := User.query.filter_by(username=username).first()):
		return redirect(url_for('login'))

	if not user.check_password(password):
		return redirect(url_for('login'))

	login_user(user)

	student = Student.query.filter_by(username=current_user.username).first()

	if student:
		return redirect(url_for('student_dash'))
	return redirect(url_for('mentor_dash'))


@app.route('/student_dash')
@login_required
@roles_required('student')
def student_dash():
	student = Student.query.filter_by(
		username=current_user.username
	).first()

	return render_template('dash/student_dash.html', student=student, team=student.team)

@app.route('/mentor_dash')
@login_required
@roles_required('mentor')
def mentor_dash():
	mentor = Mentor.query.filter_by(
		username=current_user.username
	).first()

	return render_template('dash/mentor_dash.html', mentor=mentor, teams=mentor.teams)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


# API?

@app.route('/user/<username>')
def get_user(username):
	if user := User.query.filter_by(username=username).first():
		return jsonify(dict(user=user.username))
	return jsonify(dict(user=None))
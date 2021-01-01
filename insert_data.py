import csv
from app.models import User, Team, Student, Mentor, Role, UserRole

def memory_to_csv(filename, data):
	with open(filename, 'w') as f:
		writer = csv.DictWriter(f, fieldnames=[k for k in data[0]])

		writer.writeheader()

		for item in data:
			writer.writerow(item)

def csv_to_db(db):
	file_associations = {
		'users': User,
		'roles': Role,
		'students': Student,
		'mentors': Mentor,
		'teams': Team,
	}

	for file, model in file_associations.items():
		with open(f'data/{file}.csv') as f:
			for row in csv.DictReader(f):
				db.session.add(model(**row))

def assign_student_roles(db, role_id):
	for student in Student.query.all():
		user = User.query.filter_by(username=student.username).first()
		db.session.add(UserRole(user_id=user.id, role_id=role_id))

def assign_mentor_roles(db, role_id):
	for mentor in Mentor.query.all():
		user = User.query.filter_by(username=mentor.username).first()
		db.session.add(UserRole(user_id=user.id, role_id=role_id))
from app import db, app
from insert_data import csv_to_db, assign_mentor_roles, assign_student_roles, make_admin

db.init_app(app)

if __name__ == "__main__":
	with app.app_context():
		db.drop_all()
		db.create_all()

		csv_to_db(db)
		assign_student_roles(db, 3)
		assign_mentor_roles(db, 4)
		make_admin(db, 'hp')

		db.session.commit()

# Add Coloumns   add_columns()
from sqlalchemy.orm import sessionmaker, relationship
from .query_2 import Student,Fee,stmt,session


students = Student()


# from sqlalchemy.orm import joinedload
# students = session.query(Student).options(joinedload(Student.fees)).all()


for student in students:
    print(f'{student.name} ({student.age}):')



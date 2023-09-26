# Add Coloumns   add_columns()
from .query_2 import Student,Fee,stmt,session


students = session.query(Student).all
for student in students:
    print(student.name)



# from sqlalchemy.orm import joinedload
# students = session.query(Student).options(joinedload(Student.fees)).all()






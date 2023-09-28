from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn",Integer,primary_key=True)
    firstname = Column("firstname",String)
    lastname = Column("lastname", String)
    gender = Column("gender",CHAR)
    age = Column("age",Integer)

    def __init__(self,ssn,first,last,gender,age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"
    
class Things(Base):
    __tablename__ = 'things'
    tid = Column('tid',Integer,primary_key=True)
    description = Column('description',String)
    owner = Column(Integer,ForeignKey('people.ssn'))


    def __init__(self,tid,description,owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f'({self.tid}) {self.description} Owned by {self.owner}'
    


engine = create_engine("sqlite:///person.db",echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# person = Person(1,'kaushal','pandey','M',20)
# session.add(person)
# person1 = [
#     Person(2,'rahul','pandey','M',20),
#     Person(3,'ramesh','pandey','M',22),
#     Person(4,'pooja','sharam','F',24),
#     Person(5,'Riya','dubey','F',26),
#     Person(6,'Uma','sharma','F',27),
#     Person(7,'Damon','salvatore','M',60),
#     Person(8,'Stefan','salvatore','M',23)
# ]

# for i in range(len(person1)):
#     session.add(person1[i])

# # session.commit()

# things1 = Things(1,"Car",person.ssn)
# things2 = Things(2,"bike",2)
# things3 = Things(3,"laptop",3)
# things4 = Things(4,"bike",4)
# things5 = Things(5,"Car",5)
# things6 = Things(6,"laptop",6)
# things7 = Things(7,"mobile",7)
# things8 = Things(8,"watch",8)

# session.add(things1)
# session.add(things2)
# session.add(things3)
# session.add(things4)
# session.add(things5)
# session.add(things6)
# session.add(things7)
# session.add(things8)

# session.commit()

# results = session.query(Person).all()
# print(results)

# for person in results:
#     print(person.firstname)


# filter_result = session.query(Person).filter(Person.gender=='M')
# for record in filter_result:
#     print(record.firstname,"--",record.lastname)


# filter_by_chr = session.query(Person).filter(Person.firstname.like("%ra%"))
# for r in filter_by_chr:
#     print(r.firstname,"--",r.age)



# filter_by_name = session.query(Person).filter(Person.firstname.in_(['kaushal','Stefan']))
# for r in filter_by_name:
#     print(r.firstname,"--",r.lastname)


things_result = session.query(Things,Person).filter(Things.owner == Person.ssn).filter(Person.firstname == "Damon").all()
for r in things_result:
    print(r)

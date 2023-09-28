# 3 type of the methods
# instance methods  = Used to access or modify the object state. 
# class methods 
# static methods 

class Student:
    school = 'DAVV' # class variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2    # instance variable 
        self.m3 = m3


    def avg(self): # instance method 
        return (self.m1 + self.m2 + self.m3)/3
    
    def get_m1(self): # instance method 
        return self.m1
    
    def set_m1(self,value): # instance method 
        self.m1 = value

    @classmethod # calss method 
    def info(cls):
        return cls.school
    
    @classmethod # class method
    def set_info(cls,value):
         cls.school = value

    @staticmethod
    def details():
        print('this is static method')

s1 = Student(21,43,65)
s2 = Student(54,76,98)

print(s1.avg())
print(s2.avg())

print(s1.get_m1())

s1.set_m1(34)
print(s1.get_m1())
 
print(Student.info())

Student.set_info('RGPV')

print(Student.info())

Student.details()
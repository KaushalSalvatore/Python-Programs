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

''' Instance methods : Instance methods are the most used methods in a Python class. 
These methods are only accessible through class objects. If we want to modify any class variable, 
this should be done inside an instance method.
The first parameter in these methods is self. self is used to refer to the current class object’s 
properties and attributes.

'''
class Cricket:
    teamName = None

    def setTeamName(self, name):
        self.teamName = name
    
    def getTeamName(self):
        return self.teamName

c = Cricket()
c.setTeamName('India')
print(c.getTeamName())

'''
Class methods are usually used to access class variables. You can call these methods directly 
using the class name instead of creating an object of that class.
To declare a class method, we need to use the @classmethod decorator. Also, as in the case of 
instance methods, self is the keyword used to access the class variables. In class methods,
we use use the cls variable to refer to the class.
'''

class Basketball:
  teamName = 'India'

  @classmethod
  def getTeamName(cls):
    return cls.teamName

print(Basketball.getTeamName())

'''
Static methods are usually used as a utility function or when we do not want an inherited 
class to modify a function definition. These methods do not have any relation to the class 
variables and instance variables; so, are not allowed to modify the class attributes inside a 
static method.

To declare a static method, we need to use the @staticmethod. Again, we will be using the
cls variable to refer to the class. These methods can be accessed using the class name as 
well as class objects.
'''

class Hockey:
    teamName = 'India'  

    @staticmethod
    def utility():
        print("This is a static method.")

c1 = Hockey()
c1.utility()

Hockey.utility()


class MyClass:
    def __init__(self, value):
        self.value = value
 
    @staticmethod
    def get_max_value(x, y):
        return max(x, y)
 
obj = MyClass(10)
 
print(MyClass.get_max_value(20, 30))  
 
print(obj.get_max_value(20, 30)) 
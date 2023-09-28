# Polymorphism
# 4 type of polymorphism
# Duck Type
# Operator Overloading 
# Metthod Overloading 
# Method Overriding 

#1. duck type 

class PyCharm:
    def execute(self):
        print('compiling')
        print('running')

class MyEditor:
    def execute(self):
        print('compiling')
        print('running')
        print('spell check')
        print('fast in working')

class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()

lap = Laptop()
lap.code(ide)

# if there is an object which has a method execute that it we not concered about which class object it is 
# “If it looks like a duck and quacks like a duck, it’s a duck”


class Bird:
    def fly(self):
        print("fly with wings")
  
class Airplane:
    def fly(self):
        print("fly with fuel")
  
class Fish:
    def swim(self):
        print("fish swim in sea")
  
# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane():
    obj.fly()
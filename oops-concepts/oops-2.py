# constructor
# self
# __ini__

class Person:
    def __init__(self):
        self.name = "RK"
        self.age = 30

    # def update(self):
    #     self.age = 35
    
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False



c1 = Person()
c2 = Person()
c1.age = 34
# c1.update()

print(c1.name)
print(c2.name)
print(c1.age)

if c1.compare(c2):
    print("they are same")
else:
    print("they are diffrent")



# print(id(c1))
# print(id(c2))


# id(c1) this will show you the heap memory address.
#  Cumputer() this is constructor that allocate the memroy 
#  self > its referring  to the object. we can access the attributes and methods of the class 
# compare(self,other) (who is calling , whom to comapre)
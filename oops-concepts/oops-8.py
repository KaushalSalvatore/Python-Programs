# Operator Overloading 

a = 5 
b = 6 
# print(a+b)
# print(int.__add__(a,b))

# __add__ megic method
# some example __abs__', '__add__', '__and__', '__bool__,__eq__', '__float__', '__floor__


class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other): # Operator Overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3


s1 = Student(12,43)
s2 = Student(43,65)

s3 = s1 + s2 # Student.__add__(s1,s2)
print(s3.m1,s3.m2)
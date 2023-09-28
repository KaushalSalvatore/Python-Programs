# Metthod Overloading 

class Student:
     
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2    


    def Sum(self,a=None,b=None,c=None):# Metthod Overloading 
        s = 0
        if a != None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        else: 
            s = a 

        return s
    
s1 = Student(23,45)

print(s1.Sum(2,4))



# Types of Arguments
# Possition
# keyword
# Default
# variable lenght

def add(a,b):
    return a+b

print(add(3,5)) # possition 


def Student(name,age):
    print(name)
    print(age)

Student(age=10 , name='ramesh')  # keyword (we dont kmow what parameter sequance is so we define with key)

def Person(name , age=18): # default (we dont new to pass age value it take automaticallty)
    print(name)
    print(age)

Person('harish')



def sum(*b): # variable lenght (we dont know how many arrgument passing)
    c=0
    for i in b:
        c = c+i 
    print(c)

sum(1,3,6,7,8,3)
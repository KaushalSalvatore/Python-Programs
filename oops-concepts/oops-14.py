# call by value in python

def update(x):
    x = 8 
    print("x " , x)

a = 10 
update(a)
print("a", a)

# in this it will not effect the value of a value because we are passing a value not refrance(call by value)

# call by reference
 
 
def add_more(list):
    list.append(50)
    print("Inside Function", list)
 
# Driver's code
mylist = [10,20,30,40]
 
add_more(mylist)
print("Outside Function:", mylist)

'''
in python there is there no concept because python treat everything as a object
call by value > when ever you call a function with calling a variable value not the address 
call by reference >  when ever you call a function with calling a variable  by address 
'''
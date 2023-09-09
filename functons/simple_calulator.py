def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def subtract(x,y):
    return x-y

x = int(input("first number :-"))
y = int(input("secound number :-"))


print('select option')
print('1 for addition :-')
print('2 for multiply :-')
print('3 for devide :-')
print('4 for subtraction :-')

choose = int(input("select option :-"))

if choose==1:
    print(add(x,y))

elif choose==2:
    print(multiply(x,y))

elif choose==3:
    print(divide(x,y))

elif choose==4:
    print(divide(x,y))
else:
    print('you choose wrong number')


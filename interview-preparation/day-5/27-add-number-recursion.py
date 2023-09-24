def add(x, y):
    if(y == 0):
        print(x)
        return x
    print(x,y)
    return add(x, y - 1) + 1
 
print("Sum =", add(110, 21))

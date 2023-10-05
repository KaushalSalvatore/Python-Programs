# Generators

def TopTen():
    n=1
    while n <=10:
        sq = n*n
        yield sq
        n += 1

value = TopTen()

for i in value:
    print(i)

# A generator function in Python is defined like a normal function, but whenever it needs to 
# generate a value, it does so with the yield keyword rather than return. If the body of 
# a def contains yield, the function automatically becomes a Python generator function. 
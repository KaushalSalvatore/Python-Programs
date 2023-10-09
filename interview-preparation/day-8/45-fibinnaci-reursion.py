# reurion : that means function calling it self.

def recursion(x):
    if x == 1:
        return 1
    else:
        print(x)
        return (x + recursion(x-1))

print(recursion(5))





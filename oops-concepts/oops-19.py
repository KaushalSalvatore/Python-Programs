# Map Functions :- The map() function in Python has two parameters, function and iterable. 
# The map() function is a powerful tool that allows you to apply a specified function to 
# every element within an iterable. It takes two arguments: the function you want to apply 
# and the iterable containing the elements you want to process. This function is a versatile 
# way to perform operations on multiple items simultaneously, making your code more efficient 
# and concise

def calculateSq(n):
    return n*n

numbers = (2, 3, 4, 5)
result = map( calculateSq, numbers)
print(list(result))
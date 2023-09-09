# Q: The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
# n = 5 
# o/p = 0 1 4 9 16


if __name__ == '__main__':
    n = int(input())
    a = range(0,n)
    for b in a:
        print(b**2)

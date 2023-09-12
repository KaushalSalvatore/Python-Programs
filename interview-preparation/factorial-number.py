def factorial_number(num):
    #5 X 4 X 3 X 2 X 1
    b=1
    for a in range(1,num+1):
        b = a*b

        print(b) 

    pass

if __name__=="__main__":

    a = int(input())
    factorial_number(a)
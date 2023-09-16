def square_root(num):
    for a in range(1,len(arr)+1):
        square = a**(1/2)
        print("%.2f" % square,end=",")

if __name__=="__main__":
    
    arr = [1,2,3,4,5,6,7,8,9]
    square_root(arr)
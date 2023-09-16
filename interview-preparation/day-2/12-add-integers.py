def add_number(a,b):
    for i in range(1,a+1):      
        b = b+1
    return b 
    
     


if __name__ == "__main__":
    a = add_number(5,3)
    print(a)
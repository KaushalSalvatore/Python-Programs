# swap-number-without-third-variable.py

def swap_number(a,b):
    print("befor swap ---- a=",a)
    print("b=",b)

    a = a+b
    b = a-b
    a = a-b
    print("after swap ---- a=",a)
    print("b=",b)


if __name__ == "__main__":
    swap_number(5,3)
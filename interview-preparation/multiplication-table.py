def print_table(a):
    for b in range(1,11):
        c = a*b
        print(a, " X ", b , " = ",c)

if __name__=="__main__":
    a = int(input())
    print_table(a)

def sequenceNumber(value):
    a = range(0,value)
    for b in a:
        print(b+1,end="")
if __name__=='__main__':
    a = int(input())
    sequenceNumber(a)


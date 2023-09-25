def char_pattern():
    count = 0 
    for i in range(65,91):
        for j in range(65,i+1):
            print(chr(j), end=" ")
        print()
    print('------------------------------------------------------------')

def char_pattern_1():
    count = 0 
    for i in range(5):
        for j in range(i+1):
            print(chr(65+count), end=" ")
            count +=1
        print()

if __name__=='__main__':
    char_pattern_1()
    char_pattern()
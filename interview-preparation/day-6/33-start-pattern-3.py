def number_pattern():
    for i in range(5):
        for j in range(i+1):
            print(j+1,end=' ')
        print()

if __name__=='__main__':
    number_pattern()

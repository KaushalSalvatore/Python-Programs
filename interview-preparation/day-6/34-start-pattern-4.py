def number_pattern():
    count = 0 
    for i in range(5):
        for j in range(i+1):
            count += 1
            print(count,end=' ')
        print()

if __name__=='__main__':
    number_pattern()
num1 = int(input('enter lower number'))
num2 = int(input('enter upper number'))


for i in range(num1,num2+1):
    if i > 1:
        for num in range(2,i):
            if(i%num) == 0:
                break

        else:
            print(i)

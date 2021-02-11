num = int(input('enter the number : '))
sum = 0
if num>0:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)

else:
    print('number should be greater then 0 ')

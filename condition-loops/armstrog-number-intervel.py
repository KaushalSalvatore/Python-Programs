num1 = int(input('enter first number'))
num2 = int(input('enter secound number'))

for num in range(num1,num2+1):

    sum = 0
    temp = num
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if(num==sum):
        print(sum)


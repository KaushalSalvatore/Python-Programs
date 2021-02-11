num = int(input('enter the number : '))
a = 0
b = 1
count = 2
print(a, ",", b, end=',')
while count<num:

    c = a+b
    print(c, end=' , ')
    a=b
    b=c
    count += 1


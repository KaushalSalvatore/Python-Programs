num = int(input("Enter a number: "))
sum = 0
temp = num
order = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

print(sum)





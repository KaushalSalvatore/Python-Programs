'''Fibonacci series 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

number = 10
a = 0 
b = 1
print(a,',',b,end=', ')
for i in range(number): 

    c = a+b
    print(c,end=' , ')
    a = b
    b = c'''

'''factorial of a number

number = 5 
a = 1
for i in range(number,0,-1):
    a = a*i
    print(i,end=" X ")
    print(a)'''

''' Armstrong Number
number = 153
temp = number
sum = 0 

while temp>0:
    digit = temp%10
    sum += digit**3
    temp //= 10

print(sum)
if number == sum :
    print('number is armstrong')
else:
    print('number is not armstrong')'''

'''prime number

number = 15

for i in range(2,number):
    if number % i == 0:
        print('number is not prime')
        break
else:
    print('number prime')'''



''' 10 narutal number sum 
num = 10
a = 0
for i in range(10):
    a += i
print(a)
    '''

''' Sum of array
arr = [12, 3, 4, 15]
a = 0
for i in range(len(arr)):
    a += arr[i]
print(a)
'''

'''find largest element in an array
arr = [12, 3, 4, 15]
temp = 0 
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[j] < arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
print(arr[-1])'''

'''find the largest number is value repeated


arr = [12, 3, 4, 3, 12, 4, 15]
single_arr = []
temp = 0 
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i] > arr[j]:

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)
 
for i in arr:
   if i not in single_arr:
      single_arr.append(i)
print(single_arr)
'''

















    


# monotonic arrray is array should decreasing and increasing order 
#[6,5,4,4]
#[1,2,3,4,4]

# arr = [6,5,4,4,1]
arr = [5 ,15 ,20 ,10]
a = []
b = []
a.extend(arr)
b.extend(arr)
temp = 0 
temp1 = 0
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        if b[i] < b[j]:
            temp1 = b[i]
            b[i] = b[j]
            b[j] = temp1

if(arr == a or arr == b):
    print('array monotonic')
else:
    print('array not monotonic')

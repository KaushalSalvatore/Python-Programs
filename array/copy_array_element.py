arr1 = [1,2,3,4,5,6,7,8,9]

arr2 = [None] * len(arr1)

# arr2 = arr1.copy()

print(arr1)


for i in range(0,len(arr1)):
    arr2[i] = arr1[i];

for i in range(0,len(arr2)):
    arr2[i]
print(arr2)

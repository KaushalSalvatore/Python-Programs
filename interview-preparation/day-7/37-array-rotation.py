def rotateArray(arr,n,b):
    temp = []
    i=0
    while(i<b):
        temp.append(arr[i])
        i = i+1
    
    i = 0

    while (b < n):
        print(arr[i],'----------',arr[b])
        arr[i] = arr[b]
        i = i + 1
        b = b + 1
    arr[:] = arr[: i] + temp
    return arr



arr = [1,2,3,4,5,6,7,8,9]
print('Array after left rotation is ',end='')
a = int(input())
print(rotateArray(arr, len(arr), a))

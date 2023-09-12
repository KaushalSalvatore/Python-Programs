def max_number(arr):
    for a in range(0,len(arr)):
        for b in range(a+1,len(arr)):
            if(arr[a]>arr[b]):
                temp = arr[a]
                arr[a] = arr[b]
                arr[b] = temp
    
    for i in range(0, len(arr)):    
        print(arr[i], end=" "); 
    print()
    print(arr[-2])

if __name__=="__main__":
    temp = 0
    arr = [1,3,5,7,9,8,6,4,2]
    max_number(arr)
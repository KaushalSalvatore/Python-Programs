def max_number(arr):
    sort_arr = []
    temp = 0

    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print(arr)

    for i in arr:
        if i not in sort_arr:
            sort_arr.append(i)
    print(sort_arr)
    print(sort_arr[-2])

if __name__=='__main__':
    arr = [2,1,3,4,9,5,7,6,9,8,8,9]
    max_number(arr)
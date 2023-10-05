if __name__=='__main__':
    index = int(input())
    arr = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
    if len(arr) > index:
        # del arr[index]
        arr.pop(index)
        print(arr)
    else:
        print('enter value grater then enter size')

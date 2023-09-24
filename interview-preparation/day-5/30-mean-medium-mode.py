def median(arr):
    temp = 0
    lenght = len(arr)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    
    if lenght % 2 == 0:
        median1 = arr[lenght//2]
        median2 = arr[lenght//2 - 1]
        median = (median1 + median2)/2
        return median
    else:
        return arr[lenght//2]



def mean(arr):
    sum = 0
    lenght = len(arr)
    for i in arr:
        sum += i

    return sum/lenght

def mode(arr):
    count = 0
    freq_dict = {}
    for i in range(len(arr)):
        count=0
        for j in range(1,len(arr)):
            if(arr[i]==arr[j]):
                count += 1
        freq_dict[arr[i]] = count
    return max(freq_dict, key=freq_dict.get)

if __name__=='__main__':
    arr = [1,2,3,4,5,6,7,8,9,4,3,2,4,5,6,5,5,6,6,6,6]
    print(median(arr))
    print(mean(arr))
    print(mode(arr))
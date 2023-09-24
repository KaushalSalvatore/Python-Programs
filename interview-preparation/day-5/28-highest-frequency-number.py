def highest_frequency_number(arr):
    count = 0
    freq_dict = {}
    for i in range(len(arr)):
        count=0
        for j in range(0,len(arr)):
            if(arr[i]==arr[j]):
                count += 1
        freq_dict[arr[i]] = count

    print(freq_dict)
    print(max(freq_dict, key=freq_dict.get))

if __name__=='__main__':
    arr = [1,2,3,4,5,6,7,6,4,3,12,4,6,7,4,4]
    highest_frequency_number(arr)    
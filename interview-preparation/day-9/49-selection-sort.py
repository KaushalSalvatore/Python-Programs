# in selection sort we found min value to start to end 

def sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i , len(list)):
            if list[j] < list[minpos]:
                minpos = j
        
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp



list = [5,3,8,7,2,9]
sort(list)
print(list)
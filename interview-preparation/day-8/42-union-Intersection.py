def union(arr1,arr2):
    print('-----------Intersection----------')
    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if(arr1[i] == arr2[j]):
                print(arr1[i],end=" ")
                print()
    
    inter_list = [value for value in arr1 if value in arr2]
    print(inter_list)


def intersection(arr1,arr2):
    print('-----------union----------')

    final_list = list(set(arr1) | set(arr2))
        
    print(final_list)
        





arr1 = [1,3,5,7,9,11,13,15,17,19]
arr2 = [2,4,6,8,3,9,12,13,15,16,19]

# union(arr1,arr2)
intersection(arr1,arr2)
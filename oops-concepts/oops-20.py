# Deep copy shallow copy
# shallow copy creates a copy of the object but reference each elelment of the object
# deep copy creates a copay of the object and element of the object

import copy

list1 = [[1,2,3],[4,5,6],[7,8,9]]

list2 = copy.copy(list1)

# list2[0]=[0,0,0]
list2[0][2]=[11]
print(list1)
print(list2)

list3 = copy.deepcopy(list1)
list3[0][2]=[11]
print(list3)
# [12, 10, 5, 6, 52, 36]
# spit = 2 
# o/p = [5, 6, 52, 36,12,10]

# left to right 
arr = [12, 10, 5, 6, 52, 36]
split = 2
a = arr[:split]
arr = arr[split:] + a 
# print(arr) # left to right 


# right to left

arr1 = [12, 10, 5, 6, 52, 36]

arr1 = arr1[-split:] +arr1[split:len(arr1)]

print(arr1)



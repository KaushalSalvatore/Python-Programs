# in binary search we need arr in sorted form


pos = -1

def search(list,n):
    l = 0 # l is lower postion
    u = len(list) -1  # u is upper bound position

    while l <= u:
        mid = (l+u) // 2 # we want value in integer not in float

        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid



list = [3,6,7,9,13,16,17,77,87]
n = 3

if search(list,n):
    print('fount at',pos+1)
else:
    print('not found')
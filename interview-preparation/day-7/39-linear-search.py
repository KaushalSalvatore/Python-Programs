pos = -1

def search(list,n):
    i = 0
    while 1 < len(list):
        if list[i] == n:
            globals () ['pos'] = i
            return True
        i = i+1 

list = (12,3,4,7,56,4,54,32)
n = 4

if search(list,n):
    print('number position',pos+1)
else:
    ('number not found')
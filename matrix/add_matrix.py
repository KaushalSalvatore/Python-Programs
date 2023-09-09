a = [[1,2,3],[3,4,5],[8,9,7]]
b = [[1,2,3],[3,4,5],[8,9,7]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j]+b[i][j]
for r in result:

    print(r)

# def add_matrix(a,b):
#
#     c = a+b
#     return c
#
#
# if __name__ == '__main__':
#     a = [[1,2,3,],[3,4,5],[8,9,7]]
#     b = [[1,2,3,],[3,4,5],[8,9,7]]
#     add_matrix(a,b)
#     print(add_matrix(a,b))
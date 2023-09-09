X = [[1,2],
       [4,5],
      [7,8]]
y = [[0,0,0],[0,0,0]]
x = len(X)
for i in range(x):
    for j in range(len(X[0])):
        y[j][i] = X[i][j]

for matrix in y:
    print(matrix)
# ListOfNumbers = [x for x in range(10)]
# print(ListOfNumbers)
# #even list
#
# EvenNumbersInList = [x for x in range(10) if x%2==0]
# print(EvenNumbersInList)
#
# #odd number list
#
# OddNumeberInList = [x for x in range(10) if x%2 !=0]
# print(OddNumeberInList)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

allarr = []

fillerarr = []

oldallarr = []

oldfillerarr = []

for X in range(x+1):

    for Y in range(y+1):

        for Z in range(z+1):
            oldallarr = [X, Y, Z]
            oldfillerarr.append(oldallarr)
            if X+Y+Z != n:
                allarr = [X,Y,Z]
                fillerarr.append(allarr)

print(oldfillerarr)

print(fillerarr)
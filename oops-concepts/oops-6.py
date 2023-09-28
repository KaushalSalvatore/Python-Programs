# constructor in inheritance and Method resolution Order(MRO)

class A:

    def __init__(self):
        print('A Class init')

    def feature1(self):
        print('Claaa A feature 1')

    def feature2(self):
        print('Claaa A feature 2')

class B(A): 

    def __init__(self):
        super().__init__() # constructor in inheritance
        print('B Class init')

    def feature1(self):
        print('Claaa B feature 3')

    def feature4(self):
        print('Claaa B feature 4')


class C: 

    def __init__(self):
        super().__init__() # constructor in inheritance
        print('C Class init')

    def feature1(self):
        print('Claaa B feature 3')


class D(A,C):

    def __init__(self):
        super().__init__() # constructor in inheritance
        print('D Class init')



b = B()
d = D()

# if you create object in sub class it will first try to find  init in sub class if it is 
# not in sub class then it will call super class init method.

# but if you want to call super class init method you have to use Super() # super().__init__()
# then is will call both parent and child both init method 


# Method resolution Order(MRO) : its always work left to right 
# d = D() when you call D class it will print A or D class init method and ignore C init method because 
# its work left to right
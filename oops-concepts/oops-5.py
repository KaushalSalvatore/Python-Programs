# inheritance

class A:

    def feature1(self):
        print('Claaa A feature 1')

    def feature2(self):
        print('Claaa A feature 2')

class B(A): # single level inheritance

    def feature3(self):
        print('Claaa B feature 3')

    def feature4(self):
        print('Claaa B feature 4')

class C(B): # Multi  level inheritance

    def feature4(self):
        print('Claaa C feature 4')

class D: 
    def feature5(self):
        print('Claaa D feature 5')

class E(D,A): # Multiple inheritance

    def feature6(self):
        print('Claaa E feature 6')

B = B()
C = C()
E = E()


B.feature1()
B.feature2()
B.feature3()
B.feature4()

E.feature5()
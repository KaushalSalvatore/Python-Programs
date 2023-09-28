# Method Overriding 

class A:

    def show(self):
        print("A method")


class B(A):

    def show(self): # # Method Overriding 
        print('B method')

B = B()
B.show()

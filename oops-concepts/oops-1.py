## __ini__ 
# self

class Computer:

    def __init__(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu
        
        
    def config(self):
        print('Laptop config',self.ram,self.cpu)

com = Computer('16gb','i5')
com1 = Computer('8gb','i10')
com.config()
com1.config()

#__init__(self) > is a method that work as a constructor is initialize the method 
# and it call automatically when object call (com.config()).
#The keyword self represents the instance of a class and binds the attributes with the given arguments.



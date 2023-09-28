# inner class 

class Studnet: #outer class 

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop: # inner class 

        def __init__(self):
            self.brand = 'HP'
            self.ram = 16
        
        def show(self):
            print(self.brand,self.ram)
    
s1 = Studnet('RK',21)
s2 = Studnet('PK',54)

s1.show()
s2.show()

lap1 = s1.lap
print(lap1.show()) # self.lap = self.Laptop()
 # or 
lap2 = Studnet.Laptop() 
print(lap2.show()) # without call self.lap = self.Laptop()



# you can create objectr of inner class inside the outer class  
# lap1 = s1.lap
# print(lap1.brand) # self.lap = self.Laptop()
# or 
#you can create object of inner class outside of outer class provided you use outer class name to call it
# lap2 = Studnet.Laptop() 
# print(lap2.brand) # without call self.lap = self.Laptop()
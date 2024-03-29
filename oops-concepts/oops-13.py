#Abstract Class 
 
from abc import ABC, abstractmethod   
class Car(ABC):  
    @abstractmethod    
    def mileage(self):  
        pass  
  
class Tesla(Car):
    
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  


'''
dicrectly python dont support Abstract method thats why its supprt 
ABC (Abstract Base Class)
abstract class have atlest on abstract method 
Abstraction is used to hide the internal functionality of the function from the users.
'''
#Python property() function

class Alphabet:
    def __init__(self,value):
        self._value=value
    
    def getValue(self):
        print('Getting Value')
        return self._value
    
    def setValue(self, value):
        print('setting Value  ' + value)
        self._value = value
    
    def delValue(self):
        print('Deleting value')
        del self._value
 
    value = property(getValue, setValue, 
                     delValue)
    

x = Alphabet('KaushalPandey')
print(x.value)
 
x.value = 'us'
 
del x.value
    

# Using @property decorator

class Student:
    def __init__(self, value):
        self._value = value
 
    # getting the values
    @property
    def value(self):
        print('Getting Student value')
        return self._value
 
    # setting the values
    @value.setter
    def value(self, value):
        print('Setting Student value to ' + value)
        self._value = value
 
    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting Studentvalue')
        del self._value
 
 
# passing the value
x = Student('Peter')
print(x.value)
 
x.value = 'Diesel'
 
del x.value


'''
fget() : used to get the value of attribute
fset() : used to set the value of attribute
fdel() : used to delete the attribute value
doc()  : string that contains the documentation (docstring) for the attribute


'''
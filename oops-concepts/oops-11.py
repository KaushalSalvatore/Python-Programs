# Iterator

nums = [7,8,9,6]
it = iter(nums)
print(it.__next__()) # predefine iterator 
print(next(it)) #  both are same 

#Custom iterator

class TopTen:
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration
        
value = TopTen()

for i in value:
    print(i)




#__iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
#__next__(): The next method returns the next value for the iterable. 



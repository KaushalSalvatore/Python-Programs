#  Monkey Patching : the term monkey patch refers to dynamic (or run-time) modifications of a class or module.
# In Python, we can actually change the behavior of code at run-time.

class Greeting:
    def greet(self):
        return 'well Come'

def new_greet(self):
    return 'Hello well come to python'

Greeting.greet = new_greet
g = Greeting()
print(g.greet())
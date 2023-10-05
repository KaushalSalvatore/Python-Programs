class Characters:

    def __init__(self,char):
        self.char=char


    def reverse_slicing(self):
         print(self.char[::-1])
    
    def reverse_loop(self):
        c =''
        for i in self.char:
          
            c = i+c
        print(c)
         
    

characters = Characters("abcd")
characters.reverse_slicing()
characters.reverse_loop()
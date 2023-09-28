class Computer:
    def config(self):
        print('i5','16gb','1TB')

com = Computer()

Computer.config(com)

com.config()

#Computer.config(com) or com.config() both are same in working 
# Computer is class
# com is a object
# Computer() is a constructor 
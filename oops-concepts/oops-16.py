# **kwargs (keyword variable lenght arguments)
# if we have value in key value pair  

def person(name , **kwargs):
    print(name)

    for i,j in kwargs.items():
        print(i,j)

person('Kaushal', age=26,city='pune',mob=564838482)
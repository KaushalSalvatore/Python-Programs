def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
 
if __name__=='__main__':
    div(2,4)
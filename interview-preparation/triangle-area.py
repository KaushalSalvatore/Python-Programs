def tringle_area(a,b,c):
    #semi-perimeter of the triangle = s = (a+b+c) / 2
    #ABC = √[s × (s – a) × (s – b) × (s – c)]
    s = (a+b+c)/2
    print(s)
    area = (s* (s-a) * (s-b) * (s-c))**1/2
    print(area)
    

if __name__=="__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    tringle_area(a,b,c)

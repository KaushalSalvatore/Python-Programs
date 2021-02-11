a = float(input('enter fisrt tringle Side'))
b = float(input('enter secound tringle Side'))
c = float(input('enter third tringle Side'))

redius = (a+b+c)/2

area=(redius*(redius-a)*(redius-b)*(redius-c)) ** 0.5

print('%0.2f'%area)
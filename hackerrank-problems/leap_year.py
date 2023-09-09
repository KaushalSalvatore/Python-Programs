# Q find leap year 
# divisible by 4 and not divisible by 100 == leap year 
#  divisible by 4 and not divisible by 100 then divisible by 400 = leap year 
def leap_year(year):
    leap = False
    if((year%4) == 0):
        if((year%100)==0):
            if((year%400)==0):
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False

    return leap

if __name__ == "__main__":
    year = int(input())
    print(leap_year(year))
    

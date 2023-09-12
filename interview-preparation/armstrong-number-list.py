# 153 = 1*1*1 + 5*5*5 + 3*3*3 = 153
# 120 = 1*1*1 + 2*2*2 + 0*0*0 = 9
# 1253 = 1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723
# 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
def armstrong_number(arr):
    armstrong_list = []
    c = [arr[0]][0]
    count = 0
    temp = 0
    sum = 0 

    #method 1 
    print(len(str(c)))

    #method 2 
    while c!=0:
        c //= 10
        count+= 1 
    # print(count) 

    for a in arr:
        temp = a
        while temp > 0:
            print(temp,"---",sum)
            digit = temp%10
            sum += digit ** count
            temp //=10
        # print(sum)
        if(a == sum):
            armstrong_list.append(sum)
            # digit=0
            print(armstrong_list)
        temp=0
        sum=0



if __name__=="__main__":

    arr = [153,120,123,370,407,371,346,874,243]
    armstrong_number(arr)




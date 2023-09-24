# perfect number example = 6, 28, 496, 8128, and 33550336

def perfect_nember(num):
    sum = 0 
    for i in range(1,num):
        if(num%i == 0):
            sum +=i
            
    # print(sum)
    if(num == sum):
        return 'number is perfect'
    else:
        return 'Not perfect'

def perfect_number_list(arr_1):
    sum = 0
    arr =[]
    for i in arr_1:
        sum = 0   
        for j in range(1,i):
            if(i%j == 0):
                sum += j
              
                if(sum == i):
                    arr.append(sum)     
                else:
                    pass

    return arr
        



if __name__=='__main__':
    num = 12
    arr_1 = [6,4,28, 496, 8128, 345,33550336]
    print(perfect_nember(num))
    print(perfect_number_list(arr_1))
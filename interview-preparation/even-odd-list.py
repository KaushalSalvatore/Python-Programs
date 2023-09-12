if __name__=="__main__":
    value = [1,12,13,14,15,16,17,18,19]
    even = []
    odd = []
    sum_even = 0 
    sum_odd = 0 
    # range = range(0,len(value))
    for a in value:
        if(a%2==0):
            sum_even += a 
            even.append(a)
            # sum_even = sum + a
        else:
            sum_odd += a
            odd.append(a)
    print('Array of even number-------------',even)
    print('sum of even number-------------',sum_even)
    print('Array of Odd number-------------',odd)
    print('sum of Odd number-------------',sum_odd)


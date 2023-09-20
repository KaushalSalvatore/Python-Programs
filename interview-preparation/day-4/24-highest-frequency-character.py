def highest_frequency(str_1):
    all_frq={}
    for i in str_1:
        if i in all_frq:
            all_frq[i] += 1
        else:
            all_frq[i] = 1
    
    print(list(all_frq.keys())[0],list(all_frq.values())[0])
    
    return max(all_frq, key=all_frq.get)



if __name__=='__main__':
    str_1='success'
    print(highest_frequency(str_1))
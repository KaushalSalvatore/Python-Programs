def character_occurrence(str_1):
    all_frq={}
    for i in str_1:
        if i in all_frq:
            all_frq[i] += 1
        else:
            all_frq[i] = 1
    return all_frq

if __name__=='__main__':
    str_1='success'
    print(character_occurrence(str_1))
def common_letter(str_1,str_2):
    str_11 = str_1.replace(" ", "")
    str_22 =  str_2.replace(" ", "")
    final_str = ''
    str_new = ''
    for i in (range(0,len(str_11))):
        for j in (range(0,len(str_22))):
            if(str_11[i] == str_22[j]):
                    final_str += str_11[i]

    for chr in final_str:
        if chr not in str_new:
            str_new += chr
    print(str_new)


# using some pridefine keys we can remove duplicate words ex : fromkeys ,Counter

if __name__ == "__main__":
    str_1 = 'hello how are you'
    str_2 = 'i am fine and you'
    common_letter(str_1,str_2)


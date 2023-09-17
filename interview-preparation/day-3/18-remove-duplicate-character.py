def duplicate_str(str_1):
    new_str = ''
    for chr in str_1:
        if chr not in new_str:
            new_str += chr
    print(new_str) 



if __name__=='__main__':
    str_1 = input()
    duplicate_str(str_1)
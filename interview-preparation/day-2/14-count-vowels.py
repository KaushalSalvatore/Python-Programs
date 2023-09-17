def count_vowel(str_1):
    count = 0
    for chr in str_1:
        if((chr == 'a') or (chr == 'e') or (chr == 'i') or (chr == 'o') or (chr =='u')):
            count += 1
        else:
            count
    print(count)


if __name__=='__main__':
    str_1 = input()
    count_vowel(str_1)
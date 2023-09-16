def count_vowel(str_1):
    count = 0
    for chr in str_1:
        if chr == 'a' or 'e' or 'i' or 'o' or 'u':
            count += 1
    print(count)


if __name__=='__main__':
    str_1 = input()
    count_vowel(str_1)
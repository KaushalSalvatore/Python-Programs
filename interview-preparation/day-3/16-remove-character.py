def remove_character(str_1):
    list_1 = ['a','e','i','u','o']
    str_2 = "".join(i for i in str_1 if i not in list_1)
    print(str_2)

if __name__=='__main__':
    str_1 = 'a string is called a palindrome if the reverse of the string is the same as the original one.'
    remove_character(str_1)
    # print(str_1)
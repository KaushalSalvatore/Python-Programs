def palindrome_str(str_1):
    reverse_str = ''
    for i in range(len(str_1)-1,-1,-1):
        reverse_str += str_1[i]

    if(str_1 == reverse_str):
        return 'Palindrome word'
    else:
        return 'Not Palindrome'

# str_1[::-1]
# str_1.reverse()


if __name__ == '__main__':
    str_1 = input()
    print(palindrome_str(str_1))
    
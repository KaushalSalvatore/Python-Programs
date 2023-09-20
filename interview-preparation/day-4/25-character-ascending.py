def character_ascending(str_1):
    chars = list(str_1)
    n = len(chars)
    count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if chars[j] > chars[j+1]:
                chars[j], chars[j+1] = chars[j+1], chars[j]

    return ''.join(chars)




if __name__=='__main__':
    str_1='success'
    print(character_ascending(str_1))
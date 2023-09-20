# 1. method with word count
def count_string(str_1):
     dict_1={}
     for i in str_1:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1
    
    
     return dict_1

def anagram_string(str_1,str_2):
    if(count_string(str_1)==count_string(str_2)):
        return 'String Anagram'
    else:
        return 'String Not Anagram'
   
# 2. arrage string in ascending and dscending order then compare
def character_ascending(str_1):
    chars = list(str_1)
    n = len(chars)
    count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if chars[j] > chars[j+1]:
                chars[j], chars[j+1] = chars[j+1], chars[j]

    return ''.join(chars)

def anagram_string_ascending(str_1,str_2):
    if(character_ascending(str_1)==character_ascending(str_2)):
        return 'String Anagram'
    else:
        return 'String Not Anagram'


if __name__=='__main__':
    str_1='success'
    str_2='suscecs'
    print(anagram_string(str_1,str_2))
    print(anagram_string_ascending(str_1,str_2))
def palindrome_number(arr):
    pali_arr = []
    rev = 0
    for b in arr: 
        temp = b 
        while b != 0:
            digit = b % 10
            rev = (rev*10)+digit
            b //= 10
        if(temp==rev):
            pali_arr.append(rev)
        rev=0
    print(pali_arr)
        
            



if __name__=="__main__":

    arr = [121,232,343,454,555,123,234,567]
    palindrome_number(arr)
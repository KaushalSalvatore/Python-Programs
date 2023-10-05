#  String = abcdefg
#  arr = [1,1,2,3,4,5,6]
#  output = 23a1b1c2d3e4f5g6

def output(str,arr):
    str_len =len(str)
    sum = 0 
    op = ''
    for i in arr:
        sum +=i
    print(sum)
    str_sum = str(sum)
    print(str_len)
    res = list(str)
    res.insert(0,str(str_sum))
    res = ''.join(res)
    print(str)

    

    for i in str:
        # op += i+op
      pass


word='abcdefg'
arr=[1,1,2,3,4,5,6]
output(word,arr)
def fibinacci(n):
    # normal approch
    # a = 0
    # b = 1
    # print(a,b,end=',')
    # for i in range(1,n+1):
    #     c = a + b
    #     print(c , end=',')
    #     a=b
    #     b=c

    if n == 0 or n == 1:

        return n

        return fibinacci(n - 1) + fibinacci(n - 2)




if __name__=='__main__':
    print(fibinacci(5))
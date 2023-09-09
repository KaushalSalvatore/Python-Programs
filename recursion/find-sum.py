def find_sum(n):

    #general method
    # sum = 0
    # for i in range(1,5+1):
    #     sum += i
    #     print(sum)

    if n == 1:
        return 1
    return n + find_sum(n - 1)  #recursion





if __name__ =='__main__':
    num = int(input('take the in put :- '))
    print(find_sum(num))
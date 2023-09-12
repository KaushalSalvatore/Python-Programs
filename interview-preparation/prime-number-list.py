def prime_number(arr):
    for i in range(2,len(arr)):
        print(i)
        for j in range(2,len(arr)):
            if i%j == 0:
                break
        if i==j:
            print(i,end=",")
if __name__=="__main__":
    prime_arr = []
    for a in range(1,101):
        prime_arr.append(a)
    prime_number(prime_arr)
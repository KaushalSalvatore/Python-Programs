def left_star_pattern():
    for i in range(5):
        for j in range(i+1):
            print('*', end=' ')
        print()
    print()
    print('-----------------------------------------------------------------')

def right_star_pattern():
    print()
    k=8

    for i in range(5):
        for j in range(k):

            print(end=' ')
        k=k-2

        for j in range(0, i+1):
         
            # printing stars
            print("*", end=" ")
     
        # ending line after each row
        print("\r")

    


if __name__=='__main__':
    left_star_pattern()
    right_star_pattern()






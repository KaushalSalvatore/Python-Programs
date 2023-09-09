# reverse the number 

number = int(input('enter the number : '))
reverse_number = 0 
while(number>0):
    reminder = number%10
    reverse_number = (reverse_number*10)+reminder
    number = number//10
    
print("The reverse number is : {}".format(reverse_number))  




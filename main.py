# Pythan program to find the factorial of a number provided by the user.
# change the value for a different result
Num=7
# To take input from the user
#num=int(input("Enter a number:"))
Factorial=1
# check if the number is negative, positive or zero
If num<0:
Print("Sorry, factorial does not exist for negative numbers")
Elif num==0:
Print("The factorial of 0 is 1")
Else:
For I in range(1,num + 1):
Factorial=factorial*i
Print("The factorial of",num,"is", factorial)
'''x=int(input("Enter a number"))
if(x%2==0 and x%x==0 and x>1):
    print("Not a prime number")
else:
    print("Prime number")'''
    
    
num = int(input("Enter a number: "))

if (num == 1):
    print(num, "is not a prime number")
elif (num > 1):
   for i in range(2,num):
       if (num % i == 0):
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
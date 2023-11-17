x=int(input("Enter a number"))
if(x%2==0 and x%x==0 and x>1):
    print("Not a prime number")
else:
    print("Prime number")
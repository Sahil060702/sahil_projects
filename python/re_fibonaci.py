def fib(n=input('enter a number:')):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
print(fib)
        
    

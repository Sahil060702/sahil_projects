x=int(input('Enter a number'))
y=int(input('Enter a number'))
z=int(input('Enter a number'))
a=lambda x,y,z:max(x,y,z)
print(a(x,y,z))

b=lambda x,y,z:min(x,y,z)
print(b(x,y,z))
name=input('Enter a string:')
def ispalindrom(name):
    return name==name[::-1]
ans=ispalindrom(name)
if ans:
    print('true')
else:
    print('false')
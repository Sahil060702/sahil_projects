#Write a Python program that prints the string s without the characters located at even indices.
#If the string is empty or only has one character, print it intact
s=input("enter a string")
if len(s)<=1:
    print(s)
else:
    r=s[::2]
    print(r)
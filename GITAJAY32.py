a=int(input("Enter a number"))
r=0
while a>0:
    d=a%10
    a=a//10
    r=(r*10)+d
print(r)

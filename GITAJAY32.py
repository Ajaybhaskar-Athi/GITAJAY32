b=int(input("Enter a number"))
rev=0
while b>0:
    d=a%10
    a=a//10
    rev=(rev*10)+d
print(rev)

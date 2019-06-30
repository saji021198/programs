a=int(input())
temp=a
sum=0
while a>0:
    d=a%10
    sum=sum+d**3
    a=a//10
    if sum==temp:
        print("yes")
        break
else:
    print("no")
        

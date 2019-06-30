p,q = map(int,input().split())
for i in range (p+1,q):
    temp=i
    sum=0
    while(i>0):
        d=i%10
        sum=sum+d**3
        i=i//10
    if (sum==temp):
        print(sum,end=' ')

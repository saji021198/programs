j=int(input())
c=0
for i in range(2,j):
    if(j%i==0):
        c=1
        break
if(c==1):
    print("yes")
else:
    print("no")
        

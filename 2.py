d=str(input())
h=len(d)
i=0
f=d[ : :-1]
u=list(f)
for i in range (0,2*(h-1)):
    if(i%2==0):
        i=i+1
    else:
        u.insert(i,"-")
print("".join(u))
    

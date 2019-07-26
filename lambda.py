a=int(input())
count=0
g=[]
for i in range(a):
    s=str(input())
    for j in s:
        if (j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U' ):
            count=count+1
    g.append ([s,count])
    count=0
g.sort(key=lambda x:x[1],reverse=True)
for i in range(0,a):
    print(g[i][0])

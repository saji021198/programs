b=list(map(str,input().split()))
g=[]
for i in b:
    t=len(i)
    g.append(t)
l=max(g)
d=g.index(l)
print(b[d])

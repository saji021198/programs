z=int(input())
count=0
inp=[]
m=['a','a','b','i','k','l']
for i in range (0,z):
    inp.append(input())
for i in inp:
    s=sorted(i)
    if(m==s):
        count=count+1
print(count)

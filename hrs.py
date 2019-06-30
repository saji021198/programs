# programs
h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
if(h1>h2):
    a=h1-h2
    c=m1-m2
    print(a,c)
else:
    b=h2-h1
    d=m2-m1
    print(b,d)

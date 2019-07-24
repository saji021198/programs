d=str(input())
k=[]
for i in d:
    if i not in k:
        k.append(i)
print("".join(k))

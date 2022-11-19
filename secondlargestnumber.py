s = "dfa12321afd"
k=[]
for a in s:
    if a.isdigit():
        k.append(int(a)) if int(a) not in k else k
k.sort()
print(k[-2]) if len(k)>1 else print(-1)
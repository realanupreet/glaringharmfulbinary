n = int(input())
ans = []
for i in range(n):
    str = input()
    nmap = {}
    for s in str:
        if s in nmap:
            nmap[s] += 1
        else:
            nmap[s] = 1
    if len(nmap) == 2:
        flag = True
        for k in nmap:
            if nmap[k] == 3:
                ans.append(6)
                flag = False
            # else:
                # ans.append(4)
        if flag:
            ans.append(4)
    elif len(nmap) == 3:
        ans.append(4)
    elif len(nmap) == 4:
        ans.append(4)
    else:
        ans.append(-1)

for a in ans:
    print(a)

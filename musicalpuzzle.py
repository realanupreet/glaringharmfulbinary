n = int(input())
for m in range(n):
    a = int(input())
    s = input()
    smap = {}
    for i in range(len(s)):
        if i == 0:
            smap[s[i]+s[i+1]] = 0
        else:
            smap[s[i-1]+s[i]] = 0

    print(len(smap))

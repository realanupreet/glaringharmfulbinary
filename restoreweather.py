standard_input="""3
5 2
1 3 5 3 9
2 5 11 2 4
6 1
-1 3 -2 0 -5 -1
-4 0 -1 4 0 0
3 3
7 7 7
9 4 8
"""
t=int(input())
for i in range(t):
    n,k=[int(a) for a in input().split()]
    est=[int(a) for a in input().split()]
    act=[int(a) for a in input().split()]
    orig=est.copy()
    est.sort()
    act.sort()
    nmap={}
    for i,e in enumerate(est):
        # print(e)
        if e in nmap:
            nmap[e].append(act[i])
        else:
            nmap[e]=[act[i]]

    # print()

    # print(nmap)
    l=[]
    for o in orig:
        # print(o,nmap[o])
        l.append(nmap[o].pop(0))
    
    print(" ".join(str(m) for m in l))



# e=[1,3,5,3,9]
# a=[2,5,11,2,4]
# e.sort()
# a.sort()
# print(e,"\n",a)
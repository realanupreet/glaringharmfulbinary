standard_input="""5
5
1 0 0 1 0
4
0 1 1 1
1
0
3
1 1 1
9
1 0 0 0 1 0 0 0 1
"""
for m in range(int(input())):
    k=int(input())
    s=input()
    a="".join(s.split()).split("1")
    l=0
    for i in a:
        if i != "":
            l=max(l,len(i))
    print(l)
